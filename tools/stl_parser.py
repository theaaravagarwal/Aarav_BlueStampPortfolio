#!/usr/bin/env python3
"""
STL File Parser and Visualizer
Handles reading STL files and converting them to matplotlib-compatible meshes.
"""

import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import struct

class STLParser:
    def __init__(self):
        self.vertices = []
        self.faces = []
        self.normals = []
        
    def read_stl(self, file_path):
        """Read STL file and parse vertices and faces."""
        try:
            with open(file_path, 'rb') as f:
                # Check if it's ASCII or binary STL
                header = f.read(80)
                f.seek(0)
                
                if header.startswith(b'solid'):
                    return self._read_ascii_stl(f)
                else:
                    return self._read_binary_stl(f)
        except Exception as e:
            print(f"Error reading STL file: {e}")
            return False
    
    def _read_ascii_stl(self, f):
        """Read ASCII STL file."""
        content = f.read().decode('utf-8', errors='ignore')
        lines = content.split('\n')
        
        vertices = []
        faces = []
        normals = []
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            if line.startswith('facet normal'):
                # Parse normal
                parts = line.split()
                normal = [float(parts[2]), float(parts[3]), float(parts[4])]
                normals.append(normal)
                
                # Skip 'outer loop'
                i += 1
                
                # Parse three vertices
                face_vertices = []
                for j in range(3):
                    i += 1
                    if i < len(lines):
                        vertex_line = lines[i].strip()
                        if vertex_line.startswith('vertex'):
                            parts = vertex_line.split()
                            vertex = [float(parts[1]), float(parts[2]), float(parts[3])]
                            face_vertices.append(vertex)
                
                faces.append(face_vertices)
                
                # Skip 'endloop' and 'endfacet'
                i += 2
            else:
                i += 1
        
        self.vertices = np.array(vertices)
        self.faces = np.array(faces)
        self.normals = np.array(normals)
        
        return True
    
    def _read_binary_stl(self, f):
        """Read binary STL file."""
        # Skip header
        f.read(80)
        
        # Read triangle count
        triangle_count = int.from_bytes(f.read(4), byteorder='little')
        
        vertices = []
        faces = []
        normals = []
        
        for _ in range(triangle_count):
            # Read normal (3 floats)
            normal = struct.unpack('<3f', f.read(12))
            normals.append(normal)
            
            # Read three vertices (3 floats each)
            face_vertices = []
            for _ in range(3):
                vertex = struct.unpack('<3f', f.read(12))
                face_vertices.append(vertex)
            
            faces.append(face_vertices)
            
            # Skip attribute byte count
            f.read(2)
        
        self.vertices = np.array(vertices)
        self.faces = np.array(faces)
        self.normals = np.array(normals)
        
        return True
    
    def get_mesh_data(self):
        """Get mesh data for matplotlib plotting."""
        if len(self.faces) == 0:
            return None, None
        
        # Convert faces to matplotlib-compatible format
        mesh_vertices = []
        mesh_faces = []
        
        vertex_index = 0
        for face in self.faces:
            face_vertices = []
            for vertex in face:
                mesh_vertices.append(vertex)
                face_vertices.append(vertex_index)
                vertex_index += 1
            mesh_faces.append(face_vertices)
        
        return np.array(mesh_vertices), np.array(mesh_faces)
    
    def get_bounding_box(self):
        """Get bounding box of the mesh."""
        if len(self.faces) == 0:
            return None
        
        all_vertices = np.vstack(self.faces)
        min_coords = np.min(all_vertices, axis=0)
        max_coords = np.max(all_vertices, axis=0)
        
        return min_coords, max_coords

def create_sample_mesh():
    """Create a sample mesh for testing when STL parsing fails."""
    # Create a simple cube mesh
    vertices = np.array([
        # Front face
        [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
        # Back face
        [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]
    ])
    
    faces = np.array([
        # Front face
        [0, 1, 2], [0, 2, 3],
        # Back face
        [4, 6, 5], [4, 7, 6],
        # Left face
        [0, 3, 7], [0, 7, 4],
        # Right face
        [1, 5, 6], [1, 6, 2],
        # Top face
        [3, 2, 6], [3, 6, 7],
        # Bottom face
        [0, 4, 5], [0, 5, 1]
    ])
    
    return vertices, faces

def plot_mesh(ax, vertices, faces, color='blue', alpha=0.7, zoom=1.0):
    """Plot mesh on matplotlib 3D axis with proper scaling and centering."""
    if vertices is None or faces is None:
        return
    
    # Performance optimization: simplify mesh if too complex
    max_faces = 1000  # Limit faces for performance
    if len(faces) > max_faces:
        # Simple decimation: take every nth face
        step = len(faces) // max_faces
        faces = faces[::step]
        print(f"Simplified mesh from {len(faces) * step} to {len(faces)} faces for performance")
    
    # Create Poly3DCollection
    poly3d = []
    for face in faces:
        face_vertices = [vertices[i] for i in face]
        poly3d.append(face_vertices)
    
    collection = Poly3DCollection(poly3d, alpha=alpha, facecolor=color, edgecolor='black')
    ax.add_collection3d(collection)
    
    # Calculate bounding box and center
    if len(vertices) > 0:
        min_coords = np.min(vertices, axis=0)
        max_coords = np.max(vertices, axis=0)
        
        # Calculate center and size
        center = (min_coords + max_coords) / 2
        size = max_coords - min_coords
        max_size = np.max(size)
        
        # Add some padding (10% of the model size)
        padding = max_size * 0.1
        
        # Apply zoom factor
        zoomed_size = max_size / zoom
        
        # Set axis limits with padding, centering, and zoom
        ax.set_xlim(center[0] - zoomed_size/2 - padding, center[0] + zoomed_size/2 + padding)
        ax.set_ylim(center[1] - zoomed_size/2 - padding, center[1] + zoomed_size/2 + padding)
        ax.set_zlim(center[2] - zoomed_size/2 - padding, center[2] + zoomed_size/2 + padding)
        
        # Set equal aspect ratio based on the actual model dimensions
        if max_size > 0:
            aspect_ratios = size / max_size
            ax.set_box_aspect(aspect_ratios)

if __name__ == "__main__":
    # Test the STL parser
    parser = STLParser()
    
    # Create a test plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Create sample mesh
    vertices, faces = create_sample_mesh()
    plot_mesh(ax, vertices, faces)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Sample Mesh')
    
    plt.show() 