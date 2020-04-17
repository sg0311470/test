

import  numpy as np
import  matplotlib.pyplot as plt

# x=np.random.rand() 


# x=np.random.rand(10) 

# x=np.random.rand(5,3) 

# plt.hist(np.random.rand(1000))



# ้height = np.random.normal(170,3,1000)


# print(np.mean(้height),np.std(้height))

# x= np.random.uniform(-10,3,100)
g=np.array(['r','p','s','t'])
for _ in range(10):

    x=np.random.choice(g)
    y=np.random.choice(g)

    # print(y)

# print(y)
y=np.random.choice(g,size=10000,replace=True, p=[.2,.4,.1,.3])
u,counts= np.unique(y,return_counts=True)

plt.bar(u,counts)
plt.show()