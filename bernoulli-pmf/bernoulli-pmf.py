import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    PMF_k = lambda k,p: p if k==1 else 1-p
    if type(x)==int:
        return (np.array([PMF_k(x,p)]),p,p*(1-p))
    else:
        x=np.array(x)
        pmf = np.array([PMF_k(k,p) for k in x])
        return (pmf,p,p*(1-p))