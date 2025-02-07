import streamlit as st
import tkinter as tk
from tkinter import messagebox
import csv
import os
from datetime import datetime

class HabitTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Habit Tracker")
        self.filename = 'habits.csv'

        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Habit', 'Date', 'Status'])

        self.create_widgets()

    def create_widgets(self):
        self.habit_label = tk.Label(self.root, text="Habit:")
        self.habit_label.grid(row=0, column=0)

        self.habit_entry = tk.Entry(self.root)
        self.habit_entry.grid(row=0, column=1)

        self.add_button = tk.Button(self.root, text="Add Habit", command=self.add_habit)
        self.add_button.grid(row=0, column=2)

        self.remove_button = tk.Button(self.root, text="Remove Habit", command=self.remove_habit)
        self.remove_button.grid(row=1, column=2)

        self.check_off_button = tk.Button(self.root, text="Check Off Habit", command=self.check_off_habit)
        self.check_off_button.grid(row=2, column=2)

        self.view_button = tk.Button(self.root, text="View Habits", command=self.view_habits)
        self.view_button.grid(row=3, column=2)

        self.habits_listbox = tk.Listbox(self.root, width=50)
        self.habits_listbox.grid(row=4, column=0, columnspan=3)

    def add_habit(self):
        habit = self.habit_entry.get()
        if habit:
            with open(self.filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([habit, datetime.now().strftime('%Y-%m-%d'), 'Not Done'])
            self.habit_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Habit added successfully!")
        else:
            messagebox.showwarning("Input Error", "Please enter a habit.")

    def remove_habit(self):
        habit = self.habit_entry.get()
        if habit:
            rows = []
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                rows = list(reader)
                rows = [row for row in rows if row[0] != habit]

            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            self.habit_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Habit removed successfully!")
        else:
            messagebox.showwarning("Input Error", "Please enter a habit.")

    def check_off_habit(self):
        habit = self.habit_entry.get()
        if habit:
            rows = []
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                rows = list(reader)
                for row in rows:
                    if row[0] == habit and row[1] == datetime.now().strftime('%Y-%m-%d'):
                        row[2] = 'Done'

            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            self.habit_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Habit checked off successfully!")
        else:
            messagebox.showwarning("Input Error", "Please enter a habit.")

    def view_habits(self):
        self.habits_listbox.delete(0, tk.END)
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.habits_listbox.insert(tk.END, row)

if __name__ == '__main__':
    root = tk.Tk()
    app = HabitTrackerGUI(root)
    root.mainloop()
