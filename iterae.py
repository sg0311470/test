import numpy as np
a = np.arange(0,10)*10

# for n in a:
#     # print(n)


# for i,v in enumerate(a,start=1):
#      print(i,v)


# b=np.arange(1,21).reshape(4,5)

# for r in np.ndenumerate(b):
#     print(r)


c=np.arange(1,31).reshape(3,2,5)

# print(c[0][1][3])
for n in c.flat:
    print(n)

for i,v in np.ndenumerate(c):
    print(i,v)