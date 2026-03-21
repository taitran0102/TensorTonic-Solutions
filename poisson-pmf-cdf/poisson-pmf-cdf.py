import numpy as np

def poisson_pmf_cdf(lam, k):
    import math
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    pmf_k = lambda x,y: float(np.exp(y*np.log(x)-x-np.sum(np.log(np.arange(1,y+1)))))
    cdf_k = sum([pmf_k(lam,i) for i in range(0,k+1)])
    return (pmf_k(lam,k),cdf_k)