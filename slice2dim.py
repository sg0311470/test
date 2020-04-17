import numpy as np

a = np.reshape(np.arange(1,21),(4,5))


a[1]


# print(a[1][1])

xx=list(np.ndenumerate(a))

# print(xx)

# print(a[2:4])
# print(a[:,2])
print(a[3:4,-1])
print(a[::2])

a=np.array([0,1,2,3,4,5,6])
print(a[::1])   