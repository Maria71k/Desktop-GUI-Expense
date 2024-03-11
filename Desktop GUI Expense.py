# Implementation of a desktop GUI expense tracker using Tkinter
# Users can add expenses, categorize spending, and view summaries

import tkinter as tk

class ExpenseTrackerGUI:
    def __init__(self, master):
        self.master = master
        self.expenses = {}

        self.category_entry = tk.Entry(master)
        self.category_entry.pack()
        self.amount_entry = tk.Entry(master)
        self.amount_entry.pack()
        self.add_button = tk.Button(master, text="Add Expense", command=self.add_expense)
        self.add_button.pack()
        self.summary_label = tk.Label(master, text="")
        self.summary_label.pack()

    def add_expense(self):
        category = self.category_entry.get()
        amount = float(self.amount_entry.get())
        if category not in self.expenses:
            self.expenses[category] = []
        self.expenses[category].append(amount)
        self.category_entry.delete(0, 'end')
        self.amount_entry.delete(0, 'end')

    def view_summary(self):
        summary = ""
        for category, expenses in self.expenses.items():
            total = sum(expenses)
            summary += f"{category}: ${total}\n"
        self.summary_label.config(text=summary)

root = tk.Tk()
app = ExpenseTrackerGUI(root)
root.mainloop()
