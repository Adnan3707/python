import numpy as np
arr2d=[
 [ 0 , 1 , 2 , 3],
 [ 4 , 5 , 6 , 7],
 [ 8 , 9, 10 ,11],
 [12 , 13, 14, 15],
 [16, 17, 18,19]
 ]
arr = np.array(arr2d)

print(arr[:,1])
print(arr[0,1])

# Get All Rows, Some Columns
print(arr[:,1:4])

print('step',arr[::2])

print('step 1:',arr[1:,:])