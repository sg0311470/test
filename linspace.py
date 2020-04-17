import  numpy as np

x=np.arange(1,11,2)



x=np.linspace(1,10,20)
print(x)

xx=np.linspace(0,2*np.pi,2000)

y=np.sin(xx)


import matplotlib.pyplot as plt

#config InlineBackend.figure_format='retina'


# plt.scatter(xx,y)
# plt.show()


a,b,c=(1,0,-4)
x=np.linspace(-10,10,40)

y=x*x**2 +b*x+c
plt.plot(x,y)
plt.show()