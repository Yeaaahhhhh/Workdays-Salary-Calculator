import tkinter as tk
from tkinter import messagebox
from datetime import date, timedelta

def is_valid_date(year, month, day):
    try:
        date(int(year), int(month), int(day))
        return True
    except ValueError:
        return False

def calculate_work_and_salary():
    start_year, start_month, start_day = [int(x.get()) for x in start_date_vars]
    end_year, end_month, end_day = [int(x.get()) for x in end_date_vars]

    if not (is_valid_date(start_year, start_month, start_day) and is_valid_date(end_year, end_month, end_day)):
        messagebox.showerror("Invalid Date", "Please enter valid start and end dates.")
        return

    start = date(start_year, start_month, start_day)
    end = date(end_year, end_month, end_day)

    if start > end:
        messagebox.showerror("Invalid Date", "Start date cannot be after end date.")
        return

    work_days_per_week = [cb_var.get() for cb_var in checkbox_vars]
    hours_per_day = float(hours_var.get())
    hourly_salary = float(salary_var.get())

    working_days = 0
    total_days = (end - start).days + 1

    for i in range(total_days):
        current_day = start + timedelta(days=i)
        if work_days_per_week[current_day.weekday()]:
            working_days += 1

    total_salary = working_days * hours_per_day * hourly_salary
    result_str = f"Working days: {working_days}\nTotal salary: ${total_salary:.2f}"
    result_label.config(text=result_str)

root = tk.Tk()
root.geometry("800x500")
root.title("Work Days and Salary Calculator")

start_date_label = tk.Label(root, text="Start date (YYYY MM DD):")
start_date_label.grid(row=0, column=0)
start_date_vars = [tk.StringVar() for _ in range(3)]
start_date_entries = [tk.Entry(root, textvariable=var) for var in start_date_vars]
for i, entry in enumerate(start_date_entries):
    entry.grid(row=0, column=i + 1)

end_date_label = tk.Label(root, text="End date (YYYY MM DD):")
end_date_label.grid(row=1, column=0)
end_date_vars = [tk.StringVar() for _ in range(3)]
end_date_entries = [tk.Entry(root, textvariable=var) for var in end_date_vars]
for i, entry in enumerate(end_date_entries):
    entry.grid(row=1, column=i + 1)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
checkbox_vars = [tk.BooleanVar(value=True if i < 5 else False) for i in range(7)]
checkboxes = [tk.Checkbutton(root, text=days[i], variable=checkbox_vars[i]) for i in range(7)]
for i, checkbox in enumerate(checkboxes):
    checkbox.grid(row=2, column=i)

hours_label = tk.Label(root, text="Hours per day:")
hours_label.grid(row=3, column=0)
hours_var = tk.StringVar()
hours_entry = tk.Entry(root, textvariable=hours_var)
hours_entry.grid(row=3, column=1)

salary_label = tk.Label(root, text="Hourly salary:")
salary_label.grid(row=4, column=0)
salary_var = tk.StringVar()
salary_entry = tk.Entry(root, textvariable=salary_var)
salary_entry.grid(row=4, column=1)

calculate_button = tk.Button(root, text="Calculate Work and Salary", command=calculate_work_and_salary)
calculate_button.grid(row=5, column=0)

result_label = tk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=8)

root.mainloop()