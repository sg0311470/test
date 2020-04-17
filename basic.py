# import numpy as np
# import matplotlib.pyplot as plt
# x=np.linspace(0,2*np.pi,360)
# y=np.sin(x)
# plt.scatter(x,y)
# plt.show()


# import matplotlib.pyplot as plt

# usd=[10,20,100]
# t=[]
# for u in usd:
#     t.append(u*35)
# t2=[ u * 35 for u in usd]
# t3=list(map(lambda u: u*35,usd))

# t4=np.array(usd) * 35


# a,b,c=(2,7,3)
# x = np.array([1,5,7,10,20])
# y=a*x**2+b*x+c


# plt.plot(x,y)
# plt.show()


import  numpy as np
print(np.__version__)

a=np.array([24,35,19,40])

age=[24,35,19,48]

b=np.array(age)

# print(b.ndim,b.shape)


drink=np.array(['a','b','c'])

# print(drink)



m=['w',20,'d',5]
m2=np.array(m)
# print(m2)

hw = np.array([[1,2,3],[1,2,3]])

# print(hw.shape,hw.ndim,hw.size)
# print(hw)

z=np.zeros((4,2))
z=np.ones((4,2))
# print(z)

z[:]=9
#print(z)

e=np.identity(4)

e=np.eye(4)

# print(e)

f=np.arange(1,11)
# print(f)


f2=np.arange(1,51)
# print(f2)

f3=np.reshape(f2,(10,5))
# print(f3)

f4=np.reshape(np.arange(1,51),(10,5))
# print(f4)



