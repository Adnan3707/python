import numpy as np
mylist = [1,2,3]

myarr = np.array(mylist)
print(type(myarr))

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]

myarr2 = np.array(my_matrix);
print(type(myarr2))
print('arr2',myarr2)
arr= np.arange(1,11)
print('array',arr)
print('array greate than 4',arr > 4)
print('filter arr',arr[arr > 4])

# Slicing

array_sli=np.array([[1,2,3],[10,11,12],
                    [4,5,6],[13,14,15],
                    [7,8,9],[16,17,18]
                    ])
print('sliced array',array_sli[1:2])
print('column slicing',array_sli[:,2])

#Aggragate Functions
arr_agg=np.array([1,2,3,4,5,67])
print('Sum',np.sum(arr_agg))
print('Avg',np.average(arr_agg))

#filtering
arr = np.array([5, 6, 77, 88, 45, 34, 54, 56, 22, 2, 24, 27])
result = arr[(arr > 18) & (arr < 65)]

print(result)