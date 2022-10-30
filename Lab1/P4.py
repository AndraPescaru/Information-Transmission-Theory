import numpy as np

def vector_in_matrice(matrice: np.ndarray, vector: np.ndarray) -> bool:

    for i in range(len(matrice)):
        if(np.array_equal(matrice[i],vector)):
            return True

    return False
