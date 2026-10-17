import pandas as pd

data = {
    "Name": [
        "Arjun", "Priya", "Rahul", "Neha", "Amit",
        "Sneha", "Vikram", "Anjali", "Rohan", "Kavya",
        "Arjun"
    ],
    "Age": [
        25, 29, None, 28, 42,
        31, 26, None, 30, 27,
        25
    ],
    "Department": [
        "IT", "HR", "IT", "Finance", "IT",
        "HR", "Finance", "IT", "Sales", "sales",
        "IT"
    ],
    "City": [
        "Bangalore", "Mumbai", "Delhi", "Bangalore", None,
        "Chennai", "Mumbai", "Bangalore", "Delhi", "Chennai",
        "Bangalore"
    ],
    "Salary": [
        55000, 48000, 75000, None, 95000,
        52000, 58000, 85000, None, 54000,
        55000
    ],
    "Experience": [
        2, 4, 10, 5, 15,
        7, 3, 12, 6, None,
        2
    ]
}

df = pd.DataFrame(data)

# print(df)

print(df.isnull().sum())
print(df[df["Age"].isnull()])

# df_clean = df.dropna()

# print(df_clean)

print('_______________________')

df['Age'] = df['Age'].fillna(df['Age'].mean())
print('_______________________')
print(df.isnull().sum())

