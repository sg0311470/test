import numpy as np
celcius = np.arange(0,102)
fah=celcius*1.8+32

t=np.stack((celcius,fah),axis=1)

np.savetxt('temperature.csv',t)
# np.savetxt('temperature2.csv',t,delimiter=',',fmt='%.1f',header=('cel,fah'),comments='')

s=np.loadtxt('temperature2.csv',delimiter=',',skiprows=1,usecols=(0))


print(s)