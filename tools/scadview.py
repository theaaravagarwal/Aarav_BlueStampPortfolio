#!/usr/bin/env python3
"""
3D SCAD File Viewer
A Python application to view and interact with OpenSCAD (.scad) files in 3D.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import subprocess
import os
import sys
import tempfile
import threading
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import re
import json
from pathlib import Path
from stl_parser import STLParser, plot_mesh, create_sample_mesh

class SCADViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("3D SCAD File Viewer")
        self.root.geometry("1200x800")
        
        # Variables
        self.current_file = None
        self.rendered_file = None
        self.view_angle = [30, 30]
        self.auto_render = tk.BooleanVar(value=True)
        
        # Performance optimization variables
        self.cached_mesh = None
        self.cached_vertices = None
        self.cached_faces = None
        self.last_render_time = 0
        self.render_debounce_timer = None
        
        # Check for OpenSCAD
        self.openscad_path = self.find_openscad()
        
        self.setup_ui()
        self.setup_bindings()
        
    def find_openscad(self):
        """Find OpenSCAD executable on the system."""
        possible_paths = [
            "openscad",
            "/Applications/OpenSCAD.app/Contents/MacOS/OpenSCAD",  # macOS
            "/usr/bin/openscad",
            "/usr/local/bin/openscad",
            "C:\\Program Files\\OpenSCAD\\openscad.exe",  # Windows
        ]
        
        for path in possible_paths:
            try:
                result = subprocess.run([path, "--version"], 
                                      capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    print(f"Found OpenSCAD at: {path}")
                    return path
            except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError):
                continue
        
        print("OpenSCAD not found. Please install OpenSCAD to use this viewer.")
        return None
    
    def setup_ui(self):
        """Setup the user interface."""
        # Main frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Top toolbar
        toolbar = ttk.Frame(main_frame)
        toolbar.pack(fill=tk.X, pady=(0, 5))
        
        # File operations
        ttk.Button(toolbar, text="Open SCAD File", command=self.open_file).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(toolbar, text="Reload", command=self.reload_file).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(toolbar, text="Render", command=self.render_scad).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(toolbar, text="Save STL", command=self.save_stl).pack(side=tk.LEFT, padx=(0, 5))
        
        # Auto-render checkbox
        ttk.Checkbutton(toolbar, text="Auto-render", variable=self.auto_render).pack(side=tk.LEFT, padx=(20, 5))
        
        # Fast mode checkbox
        self.fast_mode = tk.BooleanVar(value=False)
        ttk.Checkbutton(toolbar, text="Fast Mode", variable=self.fast_mode, 
                       command=self.toggle_fast_mode).pack(side=tk.LEFT, padx=(0, 5))
        
        # Status label
        self.status_label = ttk.Label(toolbar, text="Ready")
        self.status_label.pack(side=tk.RIGHT)
        
        # Performance indicator
        self.performance_label = ttk.Label(toolbar, text="", foreground="green")
        self.performance_label.pack(side=tk.RIGHT, padx=(0, 10))
        
        # Split pane for editor and viewer
        paned_window = ttk.PanedWindow(main_frame, orient=tk.HORIZONTAL)
        paned_window.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - SCAD editor
        left_frame = ttk.Frame(paned_window)
        paned_window.add(left_frame, weight=1)
        
        # SCAD file info
        ttk.Label(left_frame, text="SCAD File:").pack(anchor=tk.W, padx=5, pady=(5, 0))
        self.file_label = ttk.Label(left_frame, text="No file loaded", foreground="gray")
        self.file_label.pack(anchor=tk.W, padx=5, pady=(0, 5))
        
        # SCAD content viewer
        ttk.Label(left_frame, text="SCAD Content:").pack(anchor=tk.W, padx=5, pady=(5, 0))
        
        # Text widget with scrollbar
        text_frame = ttk.Frame(left_frame)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=(0, 5))
        
        self.text_widget = tk.Text(text_frame, wrap=tk.NONE, font=("Courier", 10))
        text_scrollbar_y = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.text_widget.yview)
        text_scrollbar_x = ttk.Scrollbar(text_frame, orient=tk.HORIZONTAL, command=self.text_widget.xview)
        self.text_widget.configure(yscrollcommand=text_scrollbar_y.set, xscrollcommand=text_scrollbar_x.set)
        
        self.text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        text_scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        text_scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Right panel - 3D viewer
        right_frame = ttk.Frame(paned_window)
        paned_window.add(right_frame, weight=2)
        
        ttk.Label(right_frame, text="3D Preview:").pack(anchor=tk.W, padx=5, pady=(5, 0))
        
        # 3D plot frame
        plot_frame = ttk.Frame(right_frame)
        plot_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=(0, 5))
        
        # Create matplotlib figure
        self.fig = Figure(figsize=(8, 6), dpi=100)
        self.ax = self.fig.add_subplot(111, projection='3d')
        
        # Embed in tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, plot_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Navigation toolbar
        toolbar_frame = ttk.Frame(plot_frame)
        toolbar_frame.pack(fill=tk.X)
        self.nav_toolbar = NavigationToolbar2Tk(self.canvas, toolbar_frame)
        self.nav_toolbar.update()
        
        # Control panel
        control_frame = ttk.LabelFrame(right_frame, text="View Controls")
        control_frame.pack(fill=tk.X, padx=5, pady=(0, 5))
        
        # View angle controls
        angle_frame = ttk.Frame(control_frame)
        angle_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(angle_frame, text="Elevation:").pack(side=tk.LEFT)
        self.elevation_var = tk.DoubleVar(value=30)
        elevation_scale = ttk.Scale(angle_frame, from_=-90, to=90, variable=self.elevation_var, 
                                   orient=tk.HORIZONTAL, command=self.update_view)
        elevation_scale.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 10))
        
        ttk.Label(angle_frame, text="Azimuth:").pack(side=tk.LEFT)
        self.azimuth_var = tk.DoubleVar(value=30)
        azimuth_scale = ttk.Scale(angle_frame, from_=0, to=360, variable=self.azimuth_var, 
                                 orient=tk.HORIZONTAL, command=self.update_view)
        azimuth_scale.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))
        
        # View preset buttons
        preset_frame = ttk.Frame(control_frame)
        preset_frame.pack(fill=tk.X, padx=5, pady=(0, 5))
        
        ttk.Button(preset_frame, text="Front", command=lambda: self.set_view(0, 0)).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(preset_frame, text="Top", command=lambda: self.set_view(90, 0)).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(preset_frame, text="Side", command=lambda: self.set_view(0, 90)).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(preset_frame, text="Isometric", command=lambda: self.set_view(35, 45)).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(preset_frame, text="Reset View", command=self.reset_view).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(preset_frame, text="Fit View", command=self.fit_view).pack(side=tk.LEFT, padx=(0, 5))
        
        # Zoom controls
        zoom_frame = ttk.Frame(control_frame)
        zoom_frame.pack(fill=tk.X, padx=5, pady=(0, 5))
        
        ttk.Label(zoom_frame, text="Zoom:").pack(side=tk.LEFT)
        self.zoom_var = tk.DoubleVar(value=1.0)
        zoom_scale = ttk.Scale(zoom_frame, from_=0.1, to=5.0, variable=self.zoom_var, 
                              orient=tk.HORIZONTAL, command=self.update_zoom)
        zoom_scale.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 10))
        
        ttk.Button(zoom_frame, text="Zoom In", command=self.zoom_in).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(zoom_frame, text="Zoom Out", command=self.zoom_out).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(zoom_frame, text="Reset Zoom", command=self.reset_zoom).pack(side=tk.LEFT, padx=(0, 5))
        
    def setup_bindings(self):
        """Setup keyboard and mouse bindings."""
        self.text_widget.bind('<KeyRelease>', self.on_text_change)
        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<Control-r>', lambda e: self.reload_file())
        self.root.bind('<F5>', lambda e: self.render_scad())
        self.root.bind('<Control-s>', lambda e: self.save_stl())
        self.root.bind('<plus>', lambda e: self.zoom_in())
        self.root.bind('<minus>', lambda e: self.zoom_out())
        self.root.bind('<equal>', lambda e: self.reset_zoom())
        self.root.bind('<Control-0>', lambda e: self.reset_zoom())
    
    def open_file(self):
        """Open a SCAD file."""
        file_path = filedialog.askopenfilename(
            title="Open SCAD File",
            filetypes=[("SCAD files", "*.scad"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                
                self.current_file = file_path
                self.file_label.config(text=os.path.basename(file_path), foreground="black")
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(1.0, content)
                
                self.status_label.config(text=f"Loaded: {os.path.basename(file_path)}")
                
                if self.auto_render.get():
                    self.render_scad()
                    
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {str(e)}")
    
    def reload_file(self):
        """Reload the current file from disk."""
        if self.current_file and os.path.exists(self.current_file):
            try:
                with open(self.current_file, 'r') as f:
                    content = f.read()
                
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(1.0, content)
                self.status_label.config(text="File reloaded")
                
                if self.auto_render.get():
                    self.render_scad()
                    
            except Exception as e:
                messagebox.showerror("Error", f"Could not reload file: {str(e)}")
        else:
            messagebox.showwarning("Warning", "No file loaded or file not found")
    
    def on_text_change(self, event=None):
        """Handle text changes in the editor with debouncing for performance."""
        if self.auto_render.get() and self.current_file:
            # Cancel previous timer if it exists
            if hasattr(self, '_render_timer') and self._render_timer:
                self.root.after_cancel(self._render_timer)
            
            # Set a new timer with longer delay for better performance
            self._render_timer = self.root.after(2000, self.render_scad)  # 2 second delay
    
    def render_scad(self):
        """Render the SCAD file to STL and display it with caching for performance."""
        if not self.openscad_path:
            messagebox.showerror("Error", "OpenSCAD not found. Please install OpenSCAD.")
            return
        
        if not self.current_file:
            messagebox.showwarning("Warning", "No SCAD file loaded")
            return
        
        # Get current content from text widget
        content = self.text_widget.get(1.0, tk.END)
        
        # Check if content has actually changed (simple hash check)
        content_hash = hash(content)
        if hasattr(self, '_last_content_hash') and self._last_content_hash == content_hash:
            # Content hasn't changed, just update the view
            if self.cached_mesh:
                self.update_display_from_cache()
                return
        
        self._last_content_hash = content_hash
        
        self.status_label.config(text="Rendering...")
        self.root.update()
        
        # Create temporary files
        with tempfile.NamedTemporaryFile(mode='w', suffix='.scad', delete=False) as temp_scad:
            temp_scad.write(content)
            temp_scad_path = temp_scad.name
        
        with tempfile.NamedTemporaryFile(suffix='.stl', delete=False) as temp_stl:
            temp_stl_path = temp_stl.name
        
        try:
            # Render SCAD to STL
            result = subprocess.run([
                self.openscad_path,
                '-o', temp_stl_path,
                temp_scad_path
            ], capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                self.rendered_file = temp_stl_path
                self.cache_mesh_data(temp_stl_path)
                self.update_display_from_cache()
                self.status_label.config(text="Rendered successfully")
            else:
                error_msg = result.stderr if result.stderr else "Unknown error"
                messagebox.showerror("Render Error", f"OpenSCAD error:\n{error_msg}")
                self.status_label.config(text="Render failed")
                
        except subprocess.TimeoutExpired:
            messagebox.showerror("Error", "Rendering timed out")
            self.status_label.config(text="Render timeout")
        except Exception as e:
            messagebox.showerror("Error", f"Rendering failed: {str(e)}")
            self.status_label.config(text="Render failed")
        finally:
            # Clean up temporary SCAD file
            try:
                os.unlink(temp_scad_path)
            except:
                pass
    
    def save_stl(self):
        """Save the rendered STL file to a user-specified location."""
        if not self.rendered_file or not os.path.exists(self.rendered_file):
            messagebox.showwarning("Warning", "No STL file to save. Please render the SCAD file first.")
            return
        
        # Get the base name from the current SCAD file
        base_name = "model"
        if self.current_file:
            base_name = os.path.splitext(os.path.basename(self.current_file))[0]
        
        file_path = filedialog.asksaveasfilename(
            title="Save STL File",
            defaultextension=".stl",
            filetypes=[("STL files", "*.stl"), ("All files", "*.*")],
            initialfile=f"{base_name}.stl"
        )
        
        if file_path:
            try:
                # Copy the temporary STL file to the user-specified location
                import shutil
                shutil.copy2(self.rendered_file, file_path)
                self.status_label.config(text=f"STL saved: {os.path.basename(file_path)}")
                messagebox.showinfo("Success", f"STL file saved successfully to:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save STL file: {str(e)}")
                self.status_label.config(text="Save failed")
    
    def display_stl(self, stl_path):
        """Display STL file in 3D viewer (legacy method - now uses caching)."""
        # This method is kept for compatibility but now uses the faster caching system
        self.cache_mesh_data(stl_path)
        self.update_display_from_cache()
    
    def update_view(self, event=None):
        """Update the 3D view angles using cached data (fast)."""
        if hasattr(self, 'ax') and self.cached_mesh:
            self.ax.view_init(self.elevation_var.get(), self.azimuth_var.get())
            self.canvas.draw()
    
    def reset_view(self):
        """Reset the 3D view to default angles."""
        self.elevation_var.set(30)
        self.azimuth_var.set(30)
        self.update_view()
    
    def set_view(self, elevation, azimuth):
        """Set the view to specific elevation and azimuth angles (fast)."""
        self.elevation_var.set(elevation)
        self.azimuth_var.set(azimuth)
        self.update_view()
    
    def fit_view(self):
        """Automatically fit the view to show the entire model."""
        if hasattr(self, 'ax') and self.cached_mesh:
            # Just update the display with current cached data
            self.update_display_from_cache()
        elif self.rendered_file:
            # If no cache but we have a rendered file, re-render once
            self.render_scad()
        else:
            # Fallback to reset view
            self.reset_view()
    
    def update_zoom(self, event=None):
        """Update the zoom level using cached data (fast)."""
        if hasattr(self, 'ax') and self.cached_mesh:
            self.update_display_from_cache()
    
    def zoom_in(self):
        """Zoom in by 20%."""
        current_zoom = self.zoom_var.get()
        new_zoom = min(5.0, current_zoom * 1.2)
        self.zoom_var.set(new_zoom)
        self.update_zoom()
    
    def zoom_out(self):
        """Zoom out by 20%."""
        current_zoom = self.zoom_var.get()
        new_zoom = max(0.1, current_zoom / 1.2)
        self.zoom_var.set(new_zoom)
        self.update_zoom()
    
    def reset_zoom(self):
        """Reset zoom to 1.0."""
        self.zoom_var.set(1.0)
        self.update_zoom()
    
    def cache_mesh_data(self, stl_path):
        """Cache the mesh data from STL file for fast rendering."""
        try:
            parser = STLParser()
            if parser.read_stl(stl_path):
                vertices, faces = parser.get_mesh_data()
                if vertices is not None and faces is not None:
                    self.cached_vertices = vertices
                    self.cached_faces = faces
                    self.cached_mesh = True
                    
                    # Update performance indicator
                    face_count = len(faces)
                    if face_count > 1000:
                        self.performance_label.config(text=f"⚡ {face_count} faces (simplified)", foreground="orange")
                    else:
                        self.performance_label.config(text=f"⚡ {face_count} faces", foreground="green")
                    
                    return True
        except Exception as e:
            print(f"Error caching mesh data: {e}")
        
        # Fallback to sample mesh
        vertices, faces = create_sample_mesh()
        self.cached_vertices = vertices
        self.cached_faces = faces
        self.cached_mesh = True
        self.performance_label.config(text="⚡ Sample mesh", foreground="blue")
        return False
    
    def update_display_from_cache(self):
        """Update the display using cached mesh data (fast)."""
        if not self.cached_mesh or self.cached_vertices is None or self.cached_faces is None:
            return
        
        try:
            self.ax.clear()
            
            # Get current zoom level
            zoom_level = self.zoom_var.get() if hasattr(self, 'zoom_var') else 1.0
            
            # Plot using cached data
            plot_mesh(self.ax, self.cached_vertices, self.cached_faces, 
                     color='lightblue', alpha=0.8, zoom=zoom_level)
            
            # Set labels and title
            self.ax.set_xlabel('X')
            self.ax.set_ylabel('Y')
            self.ax.set_zlabel('Z')
            self.ax.set_title('SCAD Model Preview')
            
            # Update the view angles
            self.ax.view_init(self.elevation_var.get(), self.azimuth_var.get())
            
            # Redraw (this is now fast since we're not re-parsing)
            self.canvas.draw()
            
        except Exception as e:
            print(f"Error updating display from cache: {e}")
            # Fallback to error display
            self.ax.clear()
            self.ax.text(0, 0, 0, 'Display Error', 
                        ha='center', va='center', fontsize=12)
            self.canvas.draw()
    
    def toggle_fast_mode(self):
        """Toggle fast mode on/off for better performance."""
        if self.fast_mode.get():
            # Fast mode: disable auto-render and increase debounce
            self.auto_render.set(False)
            self.performance_label.config(text="🚀 Fast Mode", foreground="red")
        else:
            # Normal mode: re-enable auto-render
            self.auto_render.set(True)
            if hasattr(self, 'cached_faces'):
                face_count = len(self.cached_faces)
                if face_count > 1000:
                    self.performance_label.config(text=f"⚡ {face_count} faces (simplified)", foreground="orange")
                else:
                    self.performance_label.config(text=f"⚡ {face_count} faces", foreground="green")
            else:
                self.performance_label.config(text="", foreground="green")
    
    def on_closing(self):
        """Handle application closing."""
        # Clean up temporary files
        if self.rendered_file and os.path.exists(self.rendered_file):
            try:
                os.unlink(self.rendered_file)
            except:
                pass
        self.root.destroy()

def main():
    """Main function to run the SCAD viewer."""
    root = tk.Tk()
    app = SCADViewer(root)
    
    # Handle window closing
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    
    # Start the application
    root.mainloop()

if __name__ == "__main__":
    main()
