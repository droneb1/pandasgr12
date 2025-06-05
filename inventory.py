import pandas as pd
import tkinter as tk
import os

# Read CSV file into DataFrame
file = pd.read_csv('inventory.csv')

def display_all():
    inventory_box.delete(0, tk.END)
    # Display all items from CSV file
    for index, row in file.iterrows():
        item_display = f"{row['Item_ID']} - {row['Product_Name']} ({row['Season']})"
        inventory_box.insert(tk.END, item_display)

def calculate_total():
    result_box.delete(0, tk.END)
    # Calculate total inventory value using pandas operations
    file['Total_Value'] = file['Stock_Quantity'] * file['Price']
    total_value = file['Total_Value'].sum()
    total_items = file['Stock_Quantity'].sum()
    avg_price = file['Price'].mean()
    
    result_box.insert(tk.END, f"Total Items: {total_items}")
    result_box.insert(tk.END, f"Total Value: ${total_value:,.2f}")
    result_box.insert(tk.END, f"Avg Price: ${avg_price:.2f}")

def search_item():
    search_term = search_entry.get().strip()
    result_box.delete(0, tk.END)
    
    if not search_term:
        result_box.insert(tk.END, "Please enter a search term")
        return
    
    # Use pandas string methods to search for items
    matches = file[file['Product_Name'].str.contains(search_term, case=False, na=False)]
    
    if matches.empty:
        result_box.insert(tk.END, f"No items found for '{search_term}'")
    else:
        result_box.insert(tk.END, f"Search results for '{search_term}':")
        result_box.insert(tk.END, "")
        for index, row in matches.iterrows():
            result_box.insert(tk.END, f"ID: {row['Item_ID']}")
            result_box.insert(tk.END, f"Name: {row['Product_Name']}")
            result_box.insert(tk.END, f"Price: ${row['Price']}")
            result_box.insert(tk.END, f"Stock: {row['Stock_Quantity']}")
            result_box.insert(tk.END, "---")

def show_seasonal():
    result_box.delete(0, tk.END)
    # Group by season and show counts
    seasonal_counts = file.groupby('Season')['Stock_Quantity'].sum()
    
    for season, quantity in seasonal_counts.items():
        result_box.insert(tk.END, f"{season}: {quantity} items")


root = tk.Tk()
root.title("Seasonal Inventory Manager")

info_label = tk.Label(root, text="Seasonal Warehouse Inventory\nEnter item name to search:")
info_label.grid(row=0, column=0, columnspan=2)

search_entry = tk.Entry(root, width=30)
search_entry.grid(row=1, column=0, columnspan=2, pady=5)

display_btn = tk.Button(root, text="Display All Items", command=display_all)
display_btn.grid(row=2, column=0)

search_btn = tk.Button(root, text="Search Item", command=search_item)
search_btn.grid(row=2, column=1, padx=15)

inventory_box = tk.Listbox(root, width=40)
inventory_box.grid(row=3, column=0, pady=10)

result_box = tk.Listbox(root, width=40)
result_box.grid(row=3, column=1, pady=10)

total_btn = tk.Button(root, text="Calculate Total", command=calculate_total)
total_btn.grid(row=4, column=0)

seasonal_stock_btn = tk.Button(root, text="Show Seasonal Summary", command=show_seasonal)
seasonal_stock_btn.grid(row=4, column=1, padx=15)

root.mainloop()