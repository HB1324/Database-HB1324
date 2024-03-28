"""
Program Title: Trip Cost Calculator
Author: Hunter Brown
Date Created: (01/01/2024)
Last Modified: (03/27/2024)
Description: Window-Based Program Designed to Calculate Fuel Efficiency for vehicle
Usage: python TripCostCalc.py
Dependencies: Self-Contained
License: None
FIXME- DEV Notes: ---
FIXME- ERRORS: ---
Error History Below
"""
#------------------------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox

# Functions
def round_trip_dist(half_length):
    full_length = round(half_length * 2, 2)
    return full_length

def tank_mileage(capacity, mpg):
    fuel_capacity = round(capacity * mpg, 2)
    return fuel_capacity

def fuel_cost(avg_price, gallons_consumed):
    fuel_price = round(avg_price * gallons_consumed, 2)
    return fuel_price

def fuel_consumption(trip_dist, fuel_capacity, mpg):
    step0 = (trip_dist * 2)
    step1 = round(fuel_capacity * mpg, 2)
    step2 = (step0 / step1) * 100
    step3 = round((step2 * 16.9) / 100, 2)
    return step3

def calculate():
    try:
        fuel_capacity = float(entry_fuel_capacity.get())
        avg_mpg = float(entry_avg_mpg.get())
        trip_dist = float(entry_trip_dist.get())
        avg_price = float(entry_avg_price.get())

        total_trip_dist = round_trip_dist(trip_dist)
        maximum_distance = tank_mileage(fuel_capacity, avg_mpg)
        total_fuel_consumption = fuel_consumption(trip_dist, fuel_capacity, avg_mpg)
        price_to_refuel = fuel_cost(avg_price, total_fuel_consumption)

        messagebox.showinfo("Results",
                            f"Total Trip Distance: {total_trip_dist} Miles\n"
                            f"Max Distance To Empty: {maximum_distance} Miles\n"
                            f"Total Fuel Consumption: {total_fuel_consumption} Gallons\n"
                            f"Price to Refuel: ${price_to_refuel}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")

# Create Tkinter window
window = tk.Tk()
window.title("Trip Cost Calculator")

# Create input labels and entry widgets
label_fuel_capacity = tk.Label(window, text="Fuel Capacity (Gallons):")
label_avg_mpg = tk.Label(window, text="Estimated MPG:")
label_trip_dist = tk.Label(window, text="Estimated Distance (One Way):")
label_avg_price = tk.Label(window, text="Average Price of Fuel (USD):")

entry_fuel_capacity = tk.Entry(window)
entry_avg_mpg = tk.Entry(window)
entry_trip_dist = tk.Entry(window)
entry_avg_price = tk.Entry(window)

# Create calculate button
button_calculate = tk.Button(window, text="Calculate", command=calculate)

# Place widgets in the window
label_fuel_capacity.grid(row=0, column=0, padx=10, pady=5)
entry_fuel_capacity.grid(row=0, column=1, padx=10, pady=5)
label_avg_mpg.grid(row=1, column=0, padx=10, pady=5)
entry_avg_mpg.grid(row=1, column=1, padx=10, pady=5)
label_trip_dist.grid(row=2, column=0, padx=10, pady=5)
entry_trip_dist.grid(row=2, column=1, padx=10, pady=5)
label_avg_price.grid(row=3, column=0, padx=10, pady=5)
entry_avg_price.grid(row=3, column=1, padx=10, pady=5)
button_calculate.grid(row=4, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
window.mainloop()