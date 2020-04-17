import numpy as np
from scipy import stats
w=np.array([1,2,4,3,5,5])
e=stats.mode(w)

# print(np.min(w),np.max(w),np.sum(w),np.mean(w),
# np.median(w),e[0][0],e[1][0]) 

w2=np.sort(w)[::-1]
w.sort()
# print(w2,w)

#2 dimen

a=np.reshape(np.arange(1,21),(4,5))

# print(np.mean(a[0]),np.mean(a))
# print(np.mean(a[:,1]))
# print(np.mean(a,axis=0))
# print(np.std(a,axis=1))
print(np.ptp(a),np.max(a)-np.min(a))