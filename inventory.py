import pandas as pd
import tkinter as tk
import os


root = tk.Tk()
root.title("Seasonal Inventory Manager")

root = tk.Tk()
root.title("Seasonal Inventory Manager")

info_label = tk.Label(root, text="Seasonal Warehouse Inventory\nClick buttons to view inventory data")
info_label.grid(row=0, column=0, columnspan=2)

display_btn = tk.Button(root, text="Display All Items") #command =display_all
display_btn.grid(row=1, column=0)

total_btn = tk.Button(root, text="Calculate Total") #command=calculate_total
total_btn.grid(row=1, column=1, padx=15)

inventory_box = tk.Listbox(root, width=40)
inventory_box.grid(row=2, column=0, pady=10)

result_box = tk.Listbox(root, width=40)
result_box.grid(row=2, column=1, pady=10)

low_stock_btn = tk.Button(root, text="Show Low Stock") #command=show_low_stock
low_stock_btn.grid(row=3, column=0, columnspan=2)

root.mainloop()