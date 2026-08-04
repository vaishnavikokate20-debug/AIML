import numpy as np
 #axis 0> vertical stackings
 # axis 1< horizontal stackings
arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
new_arr=np.concatenate((arr1, arr2))
print(new_arr)
