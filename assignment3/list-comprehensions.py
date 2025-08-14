#Task 3
import os
import csv

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, '../csv/employees.csv')

with open(csv_path, newline='') as file:
    reader = csv.reader(file)
    data = list(reader) # read csv file


employees = data[1:]

full_names = [row[1] + " " + row[2] for row in employees if len(row) >= 3]
print("All Names:", full_names)

# to Filter names that contain the letter "e" by 
# using list comprehension instead of the built in filter()
names_with_e = [name for name in full_names if 'e' in name]
print("Names with 'e':", names_with_e)
