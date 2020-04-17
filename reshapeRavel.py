import numpy as np 
a=np.arange(1,13)

x=a.reshape(-1,1)


a=a.ravel()
# print(a)


g=np.array([2,1,8])

x=np.tile(g,(3,1))

e=np.array([[1,2],[10,20]])

# print(np.tile(e,3))
# print(np.tile(e,(5,2)))
e=np.tile([[1,0],[0,1]],(4,4))
# print(e)


g=np.repeat([[9,3],[2,4]],3)
print(g.ravel())