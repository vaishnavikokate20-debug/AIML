import numpy as np
arr_2d=np.array([[1,2,3,4,5],[6,7,8,9,10]])  # axis = 0 == row
print(arr_2d)
new_arr_2d=np.delete(arr_2d,0,axis=0)          #  axis = 1 == column
print(new_arr_2d)
