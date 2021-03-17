import numpy as np
r = int(input()) 
lst = [float(x) for x in input().split()]
arr = np.array(lst)
arr_reshaped = arr.reshape(r,len(lst)//r)
y = np.round(arr_reshaped, 2)
print(y)
