import pandas as pd
import numpy as np

#Task 1

# 1: Create the DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
task1_data_frame = pd.DataFrame(data) # to convert the dictionary into DataFrame using pandas
print(task1_data_frame)

# 2: Make a copy and add the Salary column
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)

# 3: Make another copy and increment the Age column +1
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print(task1_older)

# 4: Save to CSV without index = False 
task1_older.to_csv('employees.csv', index=False)



#Task 2

# Load CSV data created in Task 1
task2_employees = pd.read_csv('employees.csv')
print(task2_employees)


# to Load the JSON file into a DataFrame
json_employees = pd.read_json('additional_employees.json')
print(json_employees)

# # Combine CSV and JSON DataFrames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)


#Task 3 


# to Get first 3 rows by using (head) default is (5)
first_three = more_employees.head(3)
print(first_three)

#to Get last 2 rows by using (tail)
last_two = more_employees.tail(2)
print(last_two)

# Get shape (rows, columns)
employee_shape = more_employees.shape
print(employee_shape)

# Print info summary about the DataFrame
more_employees.info()


## Task 4


# 1 Load the dirty data
dirty_data = pd.read_csv('dirty_data.csv')
print(dirty_data)

# 2 a copy for clean
clean_data = dirty_data.copy()

# 3 To Remove any duplicate rows
clean_data = clean_data.drop_duplicates()
print(clean_data)

# 4 Convert Age to numeric and handle missing values
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print(clean_data)

# 5  Convert Salary to numeric, replace 'unknown' and 'n/a' with NaN first
clean_data['Salary'] = clean_data['Salary'].str.strip()# rremoves spaces
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], np.nan)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'])
print(clean_data)

# 6  Fill missing values by using fillna method 
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())
print(clean_data)

# 7 Convert Hire Date to datetime format
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'].str.strip(), errors='coerce')
print(clean_data)

# 8 Strip extra spaces and make Name and Department uppercase
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()

print(clean_data)



#python assignment4.py
# pytest -v -x assignment4-test.py