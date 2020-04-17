import numpy as np

np.random.seed(9)
x=np.random.randint(1,11,5)

b=np.repeat(np.array([2]),5)

z=(x-np.mean(x))/ (np.std(x))
# print(x*b) 
# 2dim


a=np.arange(1,7).reshape(3,-1)*10
# print(a.shape)
# print(np.array([5])+a)
# print(np.full((3,2),5)+a)

# print(np.full(a.shape,5)+a)
# print(5+a)


c=np.array([2,10])
e=np.tile(c,a.shape[0]).reshape(a.shape)
d=np.array([[2],[3],[4]])


# print(a+d)
# print(d.shape)

e=np.array([[2,2]],[3,3],[4,4])


s=np.array([[5],[100]])
print(e+s)