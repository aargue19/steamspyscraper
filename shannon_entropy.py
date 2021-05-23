# import pandas as pd
# import scipy.stats
import sys

#!/usr/bin/env python

# Shannon Diversity Index
# http://en.wikipedia.org/wiki/Shannon_index

# https://gist.github.com/audy/783125




def sdi(data):
    
    from math import log as ln
    
    def p(n, N):
        
        if n is 0:
            return 0
        else:
            return (float(n)/N) * ln(float(n)/N)
            
    N = sum(data.values())
    
    return -sum(p(n, N) for n in data.values() if n != 0)

print(sdi({'a': 10, 'b': 20, 'c': 30,}))











# data = [1,2,2,3,3,3]

# pd_series = pd.Series(data)

# counts = pd_series.value_counts()

# entropy = scipy.stats.entropy(counts)

# print(entropy)






# import numpy as np
# def entropy(dist):
#     su=0
#     for p in dist:
#         r= p/sum(dist)
#         if r==0:
#             su+=0
#         else:
#             su+= -r*(np.log(r))
#     return su/np.log(2)

# import pandas as pd
# import scipy.stats

# def ent(data):
#     """Calculates entropy of the passed `pd.Series`
#     """
#     p_data = data.value_counts()           # counts occurrence of each value
#     entropy = scipy.stats.entropy(p_data)  # get entropy from counts
#     return entropy