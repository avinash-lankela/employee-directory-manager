# Employee Directory Manager

## Overview
    This project was developed as part of a Python Collections assignment. The objective of the assignment is to demonstrate the use of Python collection data types such as     Lists, Tuples, Sets, and Dictionaries while building a simple Employee Directory Management System.
    The program also includes user input handling and a menu-driven interface to perform basic employee management operations.

 # Question 1: Employee List Management (Lists)

## Objective
    To understand how Python Lists work and how elements can be added and removed dynamically.
## Implementation
    A list was created containing employee names.

## Operations performed:
    Added a new employee using append()
    Removed an existing employee using remove()
    Displayed the updated employee list
    Concepts Used

## List Creation
    append()
    remove()
    List Traversal

## Example
    employees = ["Avinash", "Rahul", "Priya", "Sneha", "Kiran"]
    employees.append("Arjun")
    employees.remove("Rahul")
  
# Question 2: Department Information (Tuples)

## Objective
    To understand the use of Tuples and how immutable collections work in Python.

## Implementation
    A tuple was created to store department names:
    Engineering
    Human Resources
    Finance
    Operations

## Operations performed:
    Printed all department names
    Accessed and printed the first department
    Calculated the total number of departments using len()

## Concepts Used
    Tuple Creation
    Tuple Indexing
    teration using Loop
    len() Function

## Example
    departments = ( "Engineering", "Human Resources", "Finance", "Operations" )
    print(departments[0])
    print(len(departments))

# Question 3: Employee Skills Tracking (Sets)

## Objective
    To understand how Sets store unique values and automatically remove duplicates.

 ## Operations performed:
    Displayed the set
    Observed duplicate removal
    Added a new skill using add()

## Concepts Used
    Set Creation
    Duplicate Handling
    add() Method
  
  ## Example
    skills = {"Python", "SQL", "AWS", "Python", "Spark"}
    skills.add("Docker")

## Observation
    The duplicate value "Python" appears only once because sets do not allow duplicate entries.

# Question 4: Employee Information (Dictionary)#

## Objective
    To understand how Dictionaries store data using key-value pairs.

## Implementation
    A dictionary was created to store employee details such as:
    Employee ID
    Name
    Role
    Experience
    Location

# Operations performed:
    Printed all key-value pairs
    Updated employee role
    Added a new field called Project

# Concepts Used
    Dictionary Creation
    Updating Values
    Adding New Keys
    Dictionary Traversal

# Example
    employee_info = { "Employee ID": 101, "Name": "Avinash", "Role": "Data Analyst" }
    employee_info["Role"] = "Senior Data Analyst"
    employee_info["Project"] = "Employee Directory Manager"

## Question 5: User Input

# Objective
    To understand how user input can be collected and used to update existing collections.

# Implementation
    The program accepts:
    Employee Name 
    Employee Skill

# Operations performed:
    Added the employee name to the employee list
    Added the employee skill to the skills set
    Displayed the updated collections

# Concepts Used
    input()
    Dynamic Data Entry
    Updating Lists
    Updating Sets

# Example
    emp_name = input("Enter Employee Name: ")
    emp_skill = input("Enter Employee Skill: ")
    employees.append(emp_name)
    skills.add(emp_skill)


