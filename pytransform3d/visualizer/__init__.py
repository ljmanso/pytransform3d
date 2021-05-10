"""Optional 3D renderer based on Open3D's visualizer."""
import warnings
try:
    import open3d as o3d
    from ._artists import (Artist, Line3D, Frame, Trajectory, Camera, Box,
                           Sphere, Cylinder, Mesh, Graph)
    from ._figure import figure, Figure

    __all__ = ["figure", "Figure", "Artist", "Line3D", "Frame", "Trajectory",
               "Camera", "Box", "Sphere", "Cylinder", "Mesh", "Graph"]
except ImportError:
    warnings.warn("3D visualizer is not available. Install open3d.")