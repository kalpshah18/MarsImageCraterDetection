from dataclasses import dataclass
import numpy as np

@dataclass
class EdgeSegment:
    pixels: np.ndarray
    centroid: tuple
    length: int
    area_type: str   # "light" or "shadow"

@dataclass
class CraterEllipse:
    center: tuple
    axes: tuple
    angle: float
    conic_matrix: np.ndarray