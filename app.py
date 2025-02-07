import streamlit as st
import csv
import os
from datetime import datetime

class HabitTracker:
    def __init__(self, filename='habits.csv'):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Habit', 'Date', 'Status'])

    def add_habit(self, habit):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([habit, datetime.now().strftime('%Y-%m-%d'), 'Not Done'])

    def remove_habit(self, habit):
        rows = []
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            rows = [row for row in rows if row[0] != habit]

        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    def check_off_habit(self, habit):
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

    def view_habits(self):
        habits = []
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                habits.append(row)
        return habits

tracker = HabitTracker()

st.title("Habit Tracker")

menu = ["Add Habit", "Remove Habit", "Check Off Habit", "View Habits"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Habit":
    st.subheader("Add a New Habit")
    habit = st.text_input("Enter the habit to add:")
    if st.button("Add Habit"):
        tracker.add_habit(habit)
        st.success(f"Habit '{habit}' added successfully!")

elif choice == "Remove Habit":
    st.subheader("Remove a Habit")
    habit = st.text_input("Enter the habit to remove:")
    if st.button("Remove Habit"):
        tracker.remove_habit(habit)
        st.success(f"Habit '{habit}' removed successfully!")

elif choice == "Check Off Habit":
    st.subheader("Check Off a Habit")
    habit = st.text_input("Enter the habit to check off:")
    if st.button("Check Off Habit"):
        tracker.check_off_habit(habit)
        st.success(f"Habit '{habit}' checked off successfully!")

elif choice == "View Habits":
    st.subheader("View All Habits")
    habits = tracker.view_habits()
    for habit in habits:
        st.write(habit)
