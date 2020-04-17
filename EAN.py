
import numpy as np 




def ean13(ean13):
    a=np.array(list(ean13[:12]),dtype=int)
    b=np.tile([1,3],6)
    c=a*b
    return 0 if c % 10 == 0 else 10 - (c%10)

ean13('400638133393x')
    

