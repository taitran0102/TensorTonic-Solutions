import numpy as np

def matrix_transpose(matrix):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    matrix = np.array(matrix)
    new_shape = (np.shape(matrix)[0],1)
    if len(np.shape(matrix))==2:
        new_shape = (np.shape(matrix)[1],np.shape(matrix)[0])
    
    result = np.zeros(new_shape)    
    for i in range(new_shape[1]):
        for j in range(new_shape[0]):
            result[j][i] = matrix[i][j]
    return result

    
    
