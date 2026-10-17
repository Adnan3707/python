import pandas as pd
arr2d=[
 [ 0 , 1 , 2 , 3],
 [ 4 , 5 , 6 , 7],
 [ 8 , 9, 10 ,11]
]
ds = pd.DataFrame(arr2d)
print(ds)
print('--------')
x=ds.iloc[:,1:4].values
print(x)

data = {
    "EmployeeID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": ["Arjun", "Priya", "Rahul", "Neha", "Amit",
             "Sneha", "Vikram", "Anjali", "Rohan", "Kavya"],
    "Age": [25, 29, 35, 28, 42, 31, 26, 38, 30, 27],
    "Department": ["IT", "HR", "IT", "Finance", "IT",
                   "HR", "Finance", "IT", "Sales", "Sales"],
    "City": ["Bangalore", "Mumbai", "Delhi", "Bangalore", "Hyderabad",
             "Chennai", "Mumbai", "Bangalore", "Delhi", "Chennai"],
    "Salary": [55000, 48000, 75000, 62000, 95000,
               52000, 58000, 85000, 60000, 54000],
    "Experience": [2, 4, 10, 5, 15, 7, 3, 12, 6, 4],
    "PerformanceScore": [78, 85, 92, 88, 95,
                         76, 81, 89, 74, 90]
}

df = pd.DataFrame(data)

print(df.head())
print(df[df["Age"]==25])

print(df[(df["Age"]==25) | (df["Age"] == 28) ])
print('----------------')
print(df[df["Name"].str.startswith('A')])

print('--Updating----')
# Single Value
df.loc[df["Name"]=='Arjun','Age']=27
print(df.iloc[0])
# Update based on a condition
df[df['Experience']>15 ,'Salary']*= 1.2

# replace
df[df["City"]=="Banglore"]