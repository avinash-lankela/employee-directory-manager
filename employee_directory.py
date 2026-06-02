#!/usr/bin/env python
# coding: utf-8

# In[1]:


# employee_directory.py
# Question 1 - Employee List Management
employees = ["Avinash", "Rahul", "Priya", "Sneha", "Kiran"]
# Add a new employee
employees.append("Arjun")
# Remove an employee
employees.remove("Rahul")
print("Final Employee List:")
print(employees)


# In[3]:


# Question 2 - Department Information
departments = (
    "Engineering",
    "Human Resources",
    "Finance",
    "Operations"
)
print("\nDepartments:")
for dept in departments:
    print(dept)
print("\nFirst Department:", departments[0])
print("Total Departments:", len(departments))


# In[5]:


# Question 3 - Employee Skills Tracking
skills = {"Python", "SQL", "AWS", "Python", "Spark"}
print("\nSkills Set:")
print(skills)
print("Duplicates are automatically removed in a set.")
skills.add("Docker")
print("Updated Skills Set:")
print(skills)


# In[7]:


# Question 4 - Employee Information
employee_info = {
    "Employee ID": 101,
    "Name": "Avinash",
    "Role": "Data Analyst",
    "Experience (Years)": 2,
    "Location": "Hyderabad"
}
print("\nEmployee Information:")
for key, value in employee_info.items():
    print(f"{key}: {value}")
# Update role
employee_info["Role"] = "Senior Data Analyst"
# Add project field
employee_info["Project"] = "Employee Directory Manager"
print("\nUpdated Employee Information:")
for key, value in employee_info.items():
    print(f"{key}: {value}")


# In[9]:


# Question 5 - User Input
emp_name = input("\nEnter Employee Name: ")
emp_skill = input("Enter Employee Skill: ")
employees.append(emp_name)
skills.add(emp_skill)
print("\nUpdated Employee List:")
print(employees)
print("\nUpdated Skills Set:")
print(skills)


# In[ ]:




