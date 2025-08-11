#Task 3

import csv

# Read the CSV file
with open('../csv/employees.csv', newline='') as file:
    reader = csv.reader(file)
    data = list(reader) # read csv file


employees = data[1:]

full_names = [row[1] + " " + row[2] for row in employees]
print("All Names:", full_names)

# to Filter names that contain the letter "e" by 
# using list comprehension instead of the built in filter()
names_with_e = [name for name in full_names if 'e' in name]
print("Names with 'e':", names_with_e)
