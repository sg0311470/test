import numpy as np 


a=np.random.randint(0,9999,100)

x= a% 2 == 0

x= a[(a%10 == 9) | (a>500)]


d=np.loadtxt('weather.csv',delimiter=',')

# print(d[np.where(d==28)])
 

print(d[x])
