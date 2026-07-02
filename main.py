import tkinter as tk
from tkinter import messagebox

# CLASSES

class Bill:
    def __init__(self, amount):
        self.amount = float(amount)

class Flatmate:
    def __init__(self, name, days):
        self.name = name
        self.days = float(days)

    def pays(self, bill, total_days):
        return round((self.days / total_days) * bill.amount, 2)


# ------------------ FUNCTIONS ------------------

flatmates = []

def add_flatmate():
    name = name_entry.get()
    days = days_entry.get()

    if name == "" or days == "":
        messagebox.showerror("Error", "Enter name and days")
        return

    try:
        days = float(days)
    except:
        messagebox.showerror("Error", "Days must be a number")
        return

    flatmates.append(Flatmate(name, days))
    listbox.insert(tk.END, f"{name}  ({days} days)")

    name_entry.delete(0, tk.END)
    days_entry.delete(0, tk.END)


def calculate_split():
    if amount_entry.get() == "":
        messagebox.showerror("Error", "Enter bill amount")
        return

    if len(flatmates) == 0:
        messagebox.showerror("Error", "Add at least one flatmate")
        return

    bill = Bill(amount_entry.get())
    total_days = sum(f.days for f in flatmates)

    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, "Bill Distribution:\n\n")

    for f in flatmates:
        payment = f.pays(bill, total_days)
        result_box.insert(tk.END, f"{f.name} pays: Rs {payment}\n")


def reset_all():
    flatmates.clear()
    listbox.delete(0, tk.END)
    result_box.delete("1.0", tk.END)
    amount_entry.delete(0, tk.END)


# ------------------ UI DESIGN ------------------

root = tk.Tk()
root.title("Flatmates Bill Splitter")
root.geometry("500x600")
root.config(bg="#f4f6f7")

title = tk.Label(root, text="Flatmates Bill Splitter", font=("Arial", 18, "bold"), bg="#f4f6f7")
title.pack(pady=10)

# Bill Amount
tk.Label(root, text="Total Bill Amount", bg="#f4f6f7", font=("Arial", 11)).pack()
amount_entry = tk.Entry(root, font=("Arial", 12), justify="center")
amount_entry.pack(pady=5)

# Flatmate Section
frame_inputs = tk.Frame(root, bg="#f4f6f7")
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Name", bg="#f4f6f7").grid(row=0, column=0, padx=5)
tk.Label(frame_inputs, text="Days Stayed", bg="#f4f6f7").grid(row=0, column=1, padx=5)

name_entry = tk.Entry(frame_inputs, width=18)
name_entry.grid(row=1, column=0, padx=5)

days_entry = tk.Entry(frame_inputs, width=18)
days_entry.grid(row=1, column=1, padx=5)

tk.Button(root, text="Add Flatmate", bg="#2ecc71", fg="white",
          font=("Arial", 11, "bold"), width=18, command=add_flatmate).pack(pady=8)

# List of flatmates
listbox = tk.Listbox(root, height=8, font=("Arial", 11))
listbox.pack(fill="x", padx=40, pady=5)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#f4f6f7")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Calculate Split", bg="#3498db", fg="white",
          font=("Arial", 11, "bold"), width=15, command=calculate_split).grid(row=0, column=0, padx=10)

tk.Button(btn_frame, text="Reset", bg="#e74c3c", fg="white",
          font=("Arial", 11, "bold"), width=10, command=reset_all).grid(row=0, column=1)

# Result Box
tk.Label(root, text="Result", bg="#f4f6f7", font=("Arial", 12, "bold")).pack()
result_box = tk.Text(root, height=10, font=("Arial", 11))
result_box.pack(fill="both", padx=40, pady=10)

root.mainloop()
