#!/usr/bin/env python3
"""
3D Print Timelapse Visualizer - GUI Version

A GUI tool to create timelapse visualizations of 3D printing processes from STL files.
Upload STL files, configure print settings, and view layer-by-layer printing animations.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import os
import struct
from typing import List, Tuple, Dict, Optional
import threading

class STLParser:
    """Parse STL files and extract mesh data."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.vertices = []
        self.faces = []
        self.is_binary = False
        
    def parse(self) -> Tuple[np.ndarray, np.ndarray]:
        """Parse STL file and return vertices and faces."""
        with open(self.filename, 'rb') as f:
            # Check if binary STL
            header = f.read(80)
            f.seek(0)
            
            if b'solid' in header[:5]:
                self._parse_ascii(f)
            else:
                self._parse_binary(f)
                
        return np.array(self.vertices), np.array(self.faces)
    
    def _parse_ascii(self, f):
        """Parse ASCII STL format."""
        lines = f.read().decode('utf-8').split('\n')
        
        for line in lines:
            line = line.strip()
            if line.startswith('vertex'):
                coords = line.split()[1:]
                self.vertices.append([float(x) for x in coords])
            elif line.startswith('facet normal'):
                # Start of a new face
                pass
            elif line.startswith('endfacet'):
                # End of face, create face indices
                if len(self.vertices) >= 3:
                    start_idx = len(self.vertices) - 3
                    self.faces.append([start_idx, start_idx + 1, start_idx + 2])
    
    def _parse_binary(self, f):
        """Parse binary STL format."""
        # Skip header
        f.read(80)
        
        # Read triangle count
        triangle_count = int.from_bytes(f.read(4), byteorder='little')
        
        for _ in range(triangle_count):
            # Skip normal vector
            f.read(12)
            
            # Read vertices
            for _ in range(3):
                x = struct.unpack('<f', f.read(4))[0]
                y = struct.unpack('<f', f.read(4))[0]
                z = struct.unpack('<f', f.read(4))[0]
                self.vertices.append([x, y, z])
            
            # Skip attribute byte count
            f.read(2)
            
            # Create face
            start_idx = len(self.vertices) - 3
            self.faces.append([start_idx, start_idx + 1, start_idx + 2])

class PrintSimulator:
    """Simulate 3D printing process layer by layer."""
    
    def __init__(self, vertices: np.ndarray, faces: np.ndarray, print_settings: Dict):
        self.vertices = vertices
        self.faces = faces
        self.settings = print_settings
        self.layers = []
        self.layer_heights = []
        
        # Calculate bounding box
        self.min_z = np.min(vertices[:, 2])
        self.max_z = np.max(vertices[:, 2])
        self.height = self.max_z - self.min_z
        
        # Generate layers
        self._generate_layers()
    
    def _generate_layers(self):
        """Generate layer data for the print simulation."""
        layer_height = self.settings['layer_height']
        current_z = self.min_z
        
        while current_z <= self.max_z:
            layer_vertices = []
            layer_faces = []
            
            # Find faces that intersect with this layer
            for face_idx, face in enumerate(self.faces):
                face_vertices = self.vertices[face]
                min_face_z = np.min(face_vertices[:, 2])
                max_face_z = np.max(face_vertices[:, 2])
                
                # Check if face intersects with current layer
                if min_face_z <= current_z + layer_height and max_face_z >= current_z:
                    # Add face to layer (with adjusted Z coordinates)
                    adjusted_vertices = face_vertices.copy()
                    # Clamp vertices to layer bounds
                    adjusted_vertices[:, 2] = np.clip(
                        adjusted_vertices[:, 2], 
                        current_z, 
                        current_z + layer_height
                    )
                    
                    # Add vertices to layer
                    start_idx = len(layer_vertices)
                    layer_vertices.extend(adjusted_vertices)
                    layer_faces.append([start_idx, start_idx + 1, start_idx + 2])
            
            if layer_vertices:
                self.layers.append(np.array(layer_vertices))
                self.layer_heights.append(current_z)
            
            current_z += layer_height
    
    def get_layer_at_height(self, height: float) -> Optional[np.ndarray]:
        """Get layer data at a specific height."""
        for i, layer_z in enumerate(self.layer_heights):
            if abs(layer_z - height) < self.settings['layer_height'] / 2:
                return self.layers[i]
        return None

class PrintTimelapseGUI:
    """GUI application for 3D print timelapse visualization."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("3D Print Timelapse Visualizer")
        self.root.geometry("1200x800")
        
        # Variables
        self.stl_file = tk.StringVar()
        self.vertices = None
        self.faces = None
        self.simulator = None
        self.animation = None
        self.canvas = None
        self.toolbar = None
        
        # Print settings
        self.layer_height = tk.DoubleVar(value=0.2)
        self.nozzle_diameter = tk.DoubleVar(value=0.4)
        self.print_speed = tk.DoubleVar(value=60.0)
        self.infill_density = tk.DoubleVar(value=20.0)
        self.fps = tk.IntVar(value=10)
        self.duration = tk.IntVar(value=10)
        
        # Animation state
        self.is_playing = False
        self.current_frame = 0
        self.total_frames = 0
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # File selection frame
        file_frame = ttk.LabelFrame(main_frame, text="STL File", padding="5")
        file_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Entry(file_frame, textvariable=self.stl_file, width=50).grid(row=0, column=0, padx=(0, 5))
        ttk.Button(file_frame, text="Browse", command=self.browse_file).grid(row=0, column=1)
        ttk.Button(file_frame, text="Load", command=self.load_stl).grid(row=0, column=2, padx=(5, 0))
        
        # Settings frame
        settings_frame = ttk.LabelFrame(main_frame, text="Print Settings", padding="5")
        settings_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))
        
        # Print settings
        ttk.Label(settings_frame, text="Layer Height (mm):").grid(row=0, column=0, sticky=tk.W, pady=2)
        ttk.Scale(settings_frame, from_=0.1, to=0.5, variable=self.layer_height, 
                 orient=tk.HORIZONTAL, length=200).grid(row=0, column=1, sticky=tk.W, pady=2)
        ttk.Label(settings_frame, textvariable=self.layer_height).grid(row=0, column=2, padx=(5, 0), pady=2)
        
        ttk.Label(settings_frame, text="Nozzle Diameter (mm):").grid(row=1, column=0, sticky=tk.W, pady=2)
        ttk.Scale(settings_frame, from_=0.2, to=1.0, variable=self.nozzle_diameter, 
                 orient=tk.HORIZONTAL, length=200).grid(row=1, column=1, sticky=tk.W, pady=2)
        ttk.Label(settings_frame, textvariable=self.nozzle_diameter).grid(row=1, column=2, padx=(5, 0), pady=2)
        
        ttk.Label(settings_frame, text="Print Speed (mm/s):").grid(row=2, column=0, sticky=tk.W, pady=2)
        ttk.Scale(settings_frame, from_=20, to=120, variable=self.print_speed, 
                 orient=tk.HORIZONTAL, length=200).grid(row=2, column=1, sticky=tk.W, pady=2)
        ttk.Label(settings_frame, textvariable=self.print_speed).grid(row=2, column=2, padx=(5, 0), pady=2)
        
        ttk.Label(settings_frame, text="Infill Density (%):").grid(row=3, column=0, sticky=tk.W, pady=2)
        ttk.Scale(settings_frame, from_=5, to=100, variable=self.infill_density, 
                 orient=tk.HORIZONTAL, length=200).grid(row=3, column=1, sticky=tk.W, pady=2)
        ttk.Label(settings_frame, textvariable=self.infill_density).grid(row=3, column=2, padx=(5, 0), pady=2)
        
        # Animation settings
        ttk.Label(settings_frame, text="Animation FPS:").grid(row=4, column=0, sticky=tk.W, pady=2)
        ttk.Scale(settings_frame, from_=5, to=30, variable=self.fps, 
                 orient=tk.HORIZONTAL, length=200).grid(row=4, column=1, sticky=tk.W, pady=2)
        ttk.Label(settings_frame, textvariable=self.fps).grid(row=4, column=2, padx=(5, 0), pady=2)
        
        ttk.Label(settings_frame, text="Duration (s):").grid(row=5, column=0, sticky=tk.W, pady=2)
        ttk.Scale(settings_frame, from_=5, to=30, variable=self.duration, 
                 orient=tk.HORIZONTAL, length=200).grid(row=5, column=1, sticky=tk.W, pady=2)
        ttk.Label(settings_frame, textvariable=self.duration).grid(row=5, column=2, padx=(5, 0), pady=2)
        
        # Control buttons
        control_frame = ttk.Frame(settings_frame)
        control_frame.grid(row=6, column=0, columnspan=3, pady=10)
        
        ttk.Button(control_frame, text="Generate Timelapse", command=self.generate_timelapse).grid(row=0, column=0, padx=5)
        ttk.Button(control_frame, text="Save GIF", command=self.save_gif).grid(row=0, column=1, padx=5)
        
        # Animation controls
        anim_frame = ttk.LabelFrame(settings_frame, text="Animation Controls", padding="5")
        anim_frame.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        self.play_button = ttk.Button(anim_frame, text="Play", command=self.toggle_animation)
        self.play_button.grid(row=0, column=0, padx=5)
        
        ttk.Button(anim_frame, text="Reset", command=self.reset_animation).grid(row=0, column=1, padx=5)
        
        self.progress_var = tk.StringVar(value="Ready")
        ttk.Label(anim_frame, textvariable=self.progress_var).grid(row=0, column=2, padx=10)
        
        # Model info
        info_frame = ttk.LabelFrame(settings_frame, text="Model Info", padding="5")
        info_frame.grid(row=8, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        self.info_text = tk.Text(info_frame, height=6, width=40)
        self.info_text.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # 3D visualization frame
        viz_frame = ttk.LabelFrame(main_frame, text="3D Visualization", padding="5")
        viz_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create matplotlib figure
        self.fig = plt.figure(figsize=(8, 6))
        self.ax = self.fig.add_subplot(111, projection='3d')
        
        # Embed in tkinter using pack to avoid geometry manager conflicts
        self.canvas = FigureCanvasTkAgg(self.fig, viz_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Add toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas, viz_frame)
        self.toolbar.update()
        self.toolbar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def browse_file(self):
        """Open file dialog to select STL file."""
        filename = filedialog.askopenfilename(
            title="Select STL File",
            filetypes=[("STL files", "*.stl"), ("All files", "*.*")]
        )
        if filename:
            self.stl_file.set(filename)
    
    def load_stl(self):
        """Load and parse STL file."""
        if not self.stl_file.get():
            messagebox.showerror("Error", "Please select an STL file first.")
            return
        
        try:
            self.progress_var.set("Loading STL file...")
            self.root.update()
            
            # Parse STL file
            parser = STLParser(self.stl_file.get())
            self.vertices, self.faces = parser.parse()
            
            # Display model info
            self.display_model_info()
            
            # Show initial model
            self.show_model()
            
            self.progress_var.set("STL file loaded successfully")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load STL file: {str(e)}")
            self.progress_var.set("Error loading file")
    
    def display_model_info(self):
        """Display information about the loaded model."""
        if self.vertices is None:
            return
        
        # Calculate model statistics
        min_coords = np.min(self.vertices, axis=0)
        max_coords = np.max(self.vertices, axis=0)
        dimensions = max_coords - min_coords
        volume = np.abs(np.sum(self.vertices[:, 0] * self.vertices[:, 1] * self.vertices[:, 2])) / 6
        
        info = f"""Model Statistics:
Dimensions: {dimensions[0]:.2f} x {dimensions[1]:.2f} x {dimensions[2]:.2f} mm
Volume: {volume:.2f} mm³
Vertices: {len(self.vertices)}
Faces: {len(self.faces)}
Height: {dimensions[2]:.2f} mm
Estimated layers: {int(dimensions[2] / self.layer_height.get())}"""
        
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(1.0, info)
    
    def show_model(self):
        """Display the 3D model."""
        if self.vertices is None or self.faces is None:
            return
        
        self.ax.clear()
        
        # Create polygons from faces
        polygons = []
        for face in self.faces:
            if len(face) == 3:
                polygon = [
                    self.vertices[face[0]],
                    self.vertices[face[1]],
                    self.vertices[face[2]]
                ]
                polygons.append(polygon)
        
        # Add polygons to plot
        collection = Poly3DCollection(polygons, alpha=0.7, facecolor='lightblue', edgecolor='black')
        self.ax.add_collection3d(collection)
        
        # Set labels and title
        self.ax.set_xlabel('X (mm)')
        self.ax.set_ylabel('Y (mm)')
        self.ax.set_zlabel('Z (mm)')
        self.ax.set_title('3D Model Preview')
        
        # Set view
        self.ax.view_init(elev=20, azim=45)
        
        # Calculate bounds with proper scaling
        min_coords = np.min(self.vertices, axis=0)
        max_coords = np.max(self.vertices, axis=0)
        dimensions = max_coords - min_coords
        
        # Set bounds maintaining aspect ratio
        self.ax.set_xlim(min_coords[0], max_coords[0])
        self.ax.set_ylim(min_coords[1], max_coords[1])
        self.ax.set_zlim(min_coords[2], max_coords[2])
        
        # Set equal aspect ratio for all axes to maintain proper proportions
        self.ax.set_box_aspect([dimensions[0], dimensions[1], dimensions[2]])
        
        self.canvas.draw()
    
    def generate_timelapse(self):
        """Generate the timelapse animation."""
        if self.vertices is None or self.faces is None:
            messagebox.showerror("Error", "Please load an STL file first.")
            return
        
        try:
            self.progress_var.set("Generating timelapse...")
            self.root.update()
            
            # Create print settings
            print_settings = {
                'layer_height': self.layer_height.get(),
                'nozzle_diameter': self.nozzle_diameter.get(),
                'print_speed': self.print_speed.get(),
                'infill_density': self.infill_density.get(),
                'fps': self.fps.get(),
                'duration': self.duration.get()
            }
            
            # Create simulator
            self.simulator = PrintSimulator(self.vertices, self.faces, print_settings)
            
            # Create animation
            self.create_animation()
            
            self.progress_var.set("Timelapse ready - click Play to start")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate timelapse: {str(e)}")
            self.progress_var.set("Error generating timelapse")
    
    def create_animation(self):
        """Create the matplotlib animation."""
        if self.simulator is None:
            return
        
        self.ax.clear()
        
        # Set up the plot
        self.ax.set_xlabel('X (mm)')
        self.ax.set_ylabel('Y (mm)')
        self.ax.set_zlabel('Z (mm)')
        self.ax.set_title('3D Print Timelapse')
        
        # Set consistent view
        self.ax.view_init(elev=20, azim=45)
        
        # Calculate bounds with proper scaling
        min_coords = np.min(self.vertices, axis=0)
        max_coords = np.max(self.vertices, axis=0)
        dimensions = max_coords - min_coords
        
        # Set bounds maintaining aspect ratio
        self.ax.set_xlim(min_coords[0], max_coords[0])
        self.ax.set_ylim(min_coords[1], max_coords[1])
        self.ax.set_zlim(min_coords[2], max_coords[2])
        
        # Set equal aspect ratio for all axes to maintain proper proportions
        self.ax.set_box_aspect([dimensions[0], dimensions[1], dimensions[2]])
        
        # Initialize empty collection
        self.collection = Poly3DCollection([], alpha=0.7, facecolor='lightblue', edgecolor='black')
        self.ax.add_collection3d(self.collection)
        
        # Progress text
        self.progress_text = self.ax.text2D(0.02, 0.98, '', transform=self.ax.transAxes, 
                                          fontsize=12, verticalalignment='top')
        
        # Animation parameters
        self.total_frames = self.fps.get() * self.duration.get()
        self.current_frame = 0
        
        # Create animation
        self.animation = FuncAnimation(
            self.fig, self.animate_frame, frames=self.total_frames,
            interval=1000/self.fps.get(), blit=False, repeat=False
        )
        
        self.canvas.draw()
    
    def animate_frame(self, frame):
        """Animate a single frame."""
        if self.simulator is None:
            return
        
        # Calculate progress
        progress = frame / self.total_frames
        
        # Calculate current height
        current_height = self.simulator.min_z + progress * self.simulator.height
        
        # Get all layers up to current height
        polygons = []
        for i, layer_z in enumerate(self.simulator.layer_heights):
            if layer_z <= current_height:
                layer_vertices = self.simulator.layers[i]
                for j in range(0, len(layer_vertices), 3):
                    if j + 2 < len(layer_vertices):
                        polygon = [
                            layer_vertices[j],
                            layer_vertices[j + 1],
                            layer_vertices[j + 2]
                        ]
                        polygons.append(polygon)
        
        # Update collection
        self.collection.set_verts(polygons)
        
        # Update progress text
        self.progress_text.set_text(f'Progress: {progress*100:.1f}% | Height: {current_height:.2f}mm')
        
        return self.collection, self.progress_text
    
    def toggle_animation(self):
        """Play/pause the animation."""
        if self.animation is None:
            messagebox.showwarning("Warning", "Please generate a timelapse first.")
            return
        
        if self.is_playing:
            if hasattr(self.animation, 'event_source') and self.animation.event_source is not None:
                self.animation.event_source.stop()
            self.play_button.config(text="Play")
            self.is_playing = False
        else:
            if hasattr(self.animation, 'event_source') and self.animation.event_source is not None:
                self.animation.event_source.start()
            self.play_button.config(text="Pause")
            self.is_playing = True
    
    def reset_animation(self):
        """Reset the animation to the beginning."""
        if self.animation is None:
            return
        
        # Stop animation if it's running
        if hasattr(self.animation, 'event_source') and self.animation.event_source is not None:
            self.animation.event_source.stop()
        
        self.is_playing = False
        self.play_button.config(text="Play")
        
        # Reset to first frame
        if hasattr(self.animation, 'frame_seq'):
            self.animation.frame_seq = self.animation.new_frame_seq()
        self.canvas.draw()
    
    def save_gif(self):
        """Save the animation as a GIF file."""
        if self.animation is None:
            messagebox.showwarning("Warning", "Please generate a timelapse first.")
            return
        
        filename = filedialog.asksaveasfilename(
            title="Save Animation",
            defaultextension=".gif",
            filetypes=[("GIF files", "*.gif"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                self.progress_var.set("Saving GIF...")
                self.root.update()
                
                self.animation.save(filename, writer='pillow', fps=self.fps.get())
                
                self.progress_var.set("GIF saved successfully")
                messagebox.showinfo("Success", f"Animation saved to {filename}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save GIF: {str(e)}")
                self.progress_var.set("Error saving GIF")

def main():
    """Main function to run the GUI application."""
    root = tk.Tk()
    app = PrintTimelapseGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
