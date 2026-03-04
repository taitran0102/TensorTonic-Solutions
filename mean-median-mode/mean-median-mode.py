import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    mean=np.average(x)
    if (len(x)%2==0):
        median = list(np.sort(x))[int(len(x)/2)-1]
        median+=list(np.sort(x))[int(len(x)/2)]
        median/=2
    else:
        median = list(np.sort(x))[int(len(x)/2)]
    max_freq = max(Counter(x).values())
    mode = [u for u,v in Counter(x).items() if v == max_freq][0]
    return (mean,median,mode)