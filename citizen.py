import numpy as np


def a(test_id):
    test = list(test_id)[:12]
    a=np.array(list(test),dtype=int)
    b=np.arange(13,1,-1)
    
    x=np.sum(a*b) % 11
 
    return 1-x if x<=1 else 11-x

print(a("110020107009x"))