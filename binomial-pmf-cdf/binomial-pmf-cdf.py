import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    # Write code here
    pmf_k = comb(n,k)*p**k*(1-p)**(n-k)
    cdf_k = sum([comb(n,i)*p**i*(1-p)**(n-i) for i in range(0,k+1)])
    return (pmf_k,cdf_k)