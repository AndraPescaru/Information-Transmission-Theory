import numpy as np

def normalizeaza(vector: np.ndarray) -> np.ndarray:
    return (vector - np.mean(vector, axis = 0)) / np.std(vector, axis = 0)
