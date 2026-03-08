import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    C=np.array(C)
    N = sum([float(c) for c in np.nditer(C)])

    row_sum_list = []
    for row in C:
        row_sum_list.append(int(sum(row)))

    col_sum_list = []
    for row in C.T:
        col_sum_list.append(int(sum(row)))

    E = np.zeros((len(row_sum_list),len(col_sum_list)))
    for i in range(0,len(row_sum_list)):
        for j in range(0,len(col_sum_list)):
            E[i][j]=(row_sum_list[i]*col_sum_list[j])/N
    
    C_1row=[int(i) for i in np.nditer(C)]
    E_1row=[float(e) for e in np.nditer(E)]

    chi2=sum([(c-e)**2/e for c,e in zip(C_1row,E_1row)])

    return (chi2, E)