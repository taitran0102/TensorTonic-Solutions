import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    B=[x for x in np.nditer(A)]
    new_shape = [np.shape(A)[1]]
    new_shape.append(np.shape(A)[0])
    return np.array(B).reshape(new_shape)
    
    
