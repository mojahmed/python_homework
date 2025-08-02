#Task 2
import csv
import traceback
import os
import custom_module
from datetime import datetime



def read_employees():
    data = {}
    rows = []

    try:
        with open('../csv/employees.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for index, row in enumerate(reader):
                if index == 0:
                    data["fields"] = row
                else:
                    rows.append(row)
            data["rows"] = rows
            return data

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = [
            f'File: {trace[0]}, Line: {trace[1]}, Func.Name: {trace[2]}, Message: {trace[3]}'
            for trace in trace_back
        ]
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit(1)

# global variable for the test
employees = read_employees()
print(employees)

# Task 3
employees = read_employees()

#Task 2
import csv
import traceback

def read_employees():
    data = {}
    rows = []

    try:
        with open('../csv/employees.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for index, row in enumerate(reader):
                if index == 0:
                    data["fields"] = row
                else:
                    rows.append(row)
            data["rows"] = rows
            return data

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = [
            f'File: {trace[0]}, Line: {trace[1]}, Func.Name: {trace[2]}, Message: {trace[3]}'
            for trace in trace_back
        ]
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit(1)

# global variable for the test
employees = read_employees()
print(employees)

# Task 3
employees = read_employees()

def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")
#####
# print("Fields:", employees["fields"])
# print("Employee ID Column Index:", employee_id_column)

#Task 4
def column_index(column_name):
    return employees["fields"].index(column_name)

def first_name(row_number):
    index = column_index("first_name")
    return employees["rows"][row_number][index]
print(first_name(2))


def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")
#####
# print("Fields:", employees["fields"])
# print("Employee ID Column Index:", employee_id_column)

#Task 4
def column_index(column_name):
    return employees["fields"].index(column_name)

def first_name(row_number):
    index = column_index("first_name")
    return employees["rows"][row_number][index]
print(first_name(2))

#Task 5
def employee_find(employee_id):
    def employee_match(row):
        # Convert the employee_id in the row to int and compare to input
        return int(row[employee_id_column]) == employee_id
    
    # Use filter with the inner function to find matching rows
    matches = list(filter(employee_match, employees["rows"]))
    
    return matches
print(employee_find(5))
print(employee_find(6))

#Task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches
print(employee_find_2(5))

#Task 7
def sort_by_last_name():
    # Get the index for last_name column
    last_name_index = column_index("last_name")
    
    # Sort rows in place by last_name using a lambda
    employees["rows"].sort(key=lambda row: row[last_name_index])
    
    # Return the sorted rows list
    return employees["rows"]

# Call the function to sort
sorted_rows = sort_by_last_name()

# Print just last names to check if sorting worked
print("Sorted last names:")
last_name_index = column_index("last_name")
for row in sorted_rows:
    print(row[last_name_index])

# Optional: print full dataset if you want to see everything
# print(employees)


#Task 8

def employee_dict(row):
    result = {}
    for index, field in enumerate(employees["fields"]):
        if field != "employee_id":
            result[field] = row[index]
    return result

# Example: test with the first employee row
print(employee_dict(employees["rows"][10]))


#Task 9

def all_employees_dict():
    result = {}
    id_index = column_index("employee_id")  # get index of employee_id

    for row in employees["rows"]:
        emp_id = row[id_index]  # get the ID value from the row
        result[emp_id] = employee_dict(row)  # use your previous function
    return result
###########
# Print the entire dictionary of employees
all_emps = all_employees_dict()
print(all_emps)

#Task 10

def get_this_value():
    return os.getenv("THISVALUE")
###########
print("THISVALUE is:", get_this_value())

#Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
##########
# Test it
set_that_secret("Mohammed")
print("The New secret is now:", custom_module.secret)

#Task 12

#helper function 
def read_csv_to_dict(path):
    with open(path, newline='') as file:
        reader = csv.reader(file)
        fields = next(reader)
        rows = [tuple(row) for row in reader]
    return {"fields": fields, "rows": rows}
# this how i define the read_muntes() function
def read_minutes():
    minutes1 = read_csv_to_dict("../csv/minutes1.csv")
    minutes2 = read_csv_to_dict("../csv/minutes2.csv")
    return minutes1, minutes2

#########
minutes1, minutes2 = read_minutes()
print("Minutes 1:", minutes1)
print("Minutes 2:", minutes2)

# Task 13

def create_minutes_set():
    # Convert the rows (already tuples) into sets
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])

    # Combine both sets using union
    combined_set = set1.union(set2)

    return combined_set
#############
minutes_set = create_minutes_set()
print("Minutes Set:", minutes_set)

#Task 14
def create_minutes_list():
    # Convert set to list
    minutes_raw_list = list(minutes_set)

    # Convert each date string into a datetime object
    minutes_converted = list(map(
        lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
        minutes_raw_list
    ))

    return minutes_converted
#############
minutes_list = create_minutes_list()
print(minutes_list)  # Optional: helpful for debugging

#Task 15

def write_sorted_list():
    # Sort the minutes list by the datetime (2nd item in each tuple)
    sorted_minutes = sorted(minutes_list, key=lambda x: x[1])

    # Convert datetime back to string format
    converted_minutes = list(map(
        lambda x: (x[0], x[1].strftime("%B %d, %Y")),
        sorted_minutes
    ))

    # Write to ./minutes.csv
    with open("./minutes.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(minutes1["fields"])  # Write the header
        writer.writerows(converted_minutes)  # Write the sorted data

    return converted_minutes
################
final_minutes = write_sorted_list()
print(final_minutes)  # Optional, just to check


