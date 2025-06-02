import pandas as pd
import os

print(os.listdir())

#Load the CSV file
file = pd.read_csv("employees.csv")

#Print first few rows
print(file.head())

average_salary = file['Salary'].mean()
print("Average Salary: ", average_salary)