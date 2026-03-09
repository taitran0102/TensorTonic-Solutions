import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    n=len(x)
    x=np.array(x)
    s2=(1/(n-1))*sum([(x_i-np.mean(x))**2 for x_i in x])
    s=np.sqrt(s2)
    t=(np.mean(x)-mu0)/(s/np.sqrt(n))
    return t