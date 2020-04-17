import numpy as np 

#ab=c
#b=c inv(a)
a=np.array([[1,1],[1,5]])

b=np.array([[90],[250]])


Ina=np.linalg.inv(a)



c=np.dot(Ina,b)
print(c)

d=Ina @ b

print(d)




A=np.matrix([[1,1],[1,5]])

B=np.matrix([[90],[250]])


AI = A.I

C=AI * B
print(C)