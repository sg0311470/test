import numpy as np 
a=np.reshape(np.arange(1,9),(4,2))
b=np.reshape(np.arange(1,9)*20,(4,2))


c=np.vstack((a,b,a))
# print(c)

d=np.hstack((a,b,a))
# print(d)


e=np.hsplit(d,3)
f=np.vsplit(d,2)


g=np.arange(1,11)

h=np.arange(1,11)*50


x=np.hstack((g,h))


print(np.stack((g,h,g),axis=0))