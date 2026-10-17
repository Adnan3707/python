import numpy as np
arr=np.array([45,67,556,556,774,4545,45455,555,554,33])
# print(arr[(arr == 774) | (arr < 100)])

evenOdd = np.array(['even','odd'] * 20)
print(evenOdd[evenOdd != 'odd'])

stock=np.array([2,0,1,2])
product_array=np.array(['pineapple','apple','orange','lemon'])

print(np.where(stock <= 0,'out of stock',product_array))

even=np.array([1,2,3,4,5,6,7,8,9,10,11,12])

print(np.where(even % 2 == 0,'even','odd'))

print(np.where(even % 2 == 0,'even',np.where(even == 9,even,'odd')))

price=np.array([5.75,4.34,44,2.4])
print(np.where(price > 5.80 ,np.where(price,product_array,''),'out of range'))