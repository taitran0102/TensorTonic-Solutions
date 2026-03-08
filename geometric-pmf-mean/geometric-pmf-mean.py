import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    # Write code here
    k=np.array(k)
    PMF_list=[]
    for i in k:
        PMF_i = (1-p)**(i-1)*p
        PMF_list.append(PMF_i)
    Mean = 1/p
    return (np.array(PMF_list),Mean)