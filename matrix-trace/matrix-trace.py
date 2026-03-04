import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    A=np.array(A)
    tr_A=0
    for i in range(0,A.shape[0]):
        for j in range(0,A.shape[1]):
            if j==i:
                tr_A+=A[i][j]
    return tr_A
    
