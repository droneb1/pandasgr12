import pandas as pd
import os

print(os.listdir())

#Load the CSV file
file = pd.read_csv("employees.csv")

#Print first few rows
print(file.head())

average_salary = file['Salary'].mean()
print("Average Salary: ", average_salary)

# Convert 'Join Date' column to datetime format
file['Join Date'] = pd.to_datetime(file['Join Date'])

# Sort the DataFrame by 'Join Date'
sorted_by_date = file.sort_values(by = 'Join Date')

#Print the sorted DataFrame
print("\nEmployees sorted by Join Date:")
print(sorted_by_date[['Employee Name', 'Join Date']])