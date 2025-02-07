import streamlit as st
import pandas as pd
import os
from datetime import datetime, timedelta

class HabitTracker:
    def __init__(self, filename='habits.csv'):
        self.filename = filename
        if not os.path.exists(self.filename):
            df = pd.DataFrame(columns=['Habit', 'Date', 'Status'])
            df.to_csv(self.filename, index=False)

    def add_habit(self, habit):
        df = pd.read_csv(self.filename)
        new_row = {'Habit': habit, 'Date': datetime.now().strftime('%Y-%m-%d'), 'Status': 'Not Done'}
        df = df.append(new_row, ignore_index=True)
        df.to_csv(self.filename, index=False)

    def remove_habit(self, habit):
        df = pd.read_csv(self.filename)
        df = df[df['Habit'] != habit]
        df.to_csv(self.filename, index=False)

    def check_off_habit(self, habit):
        df = pd.read_csv(self.filename)
        today = datetime.now().strftime('%Y-%m-%d')
        df.loc[(df['Habit'] == habit) & (df['Date'] == today), 'Status'] = 'Done'
        df.to_csv(self.filename, index=False)

    def view_habits(self):
        df = pd.read_csv(self.filename)
        return df

    def get_habit_progress(self, habit):
        df = pd.read_csv(self.filename)
        habit_data = df[df['Habit'] == habit]
        total_days = len(habit_data)
        completed_days = len(habit_data[habit_data['Status'] == 'Done'])
        return completed_days, total_days

tracker = HabitTracker()

st.title("Habit Tracker")

menu = ["Add Habit", "Remove Habit", "Check Off Habit", "View Habits", "Habit Progress"]
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
    st.write(habits)

elif choice == "Habit Progress":
    st.subheader("Habit Progress")
    habit = st.text_input("Enter the habit to check progress:")
    if st.button("Check Progress"):
        completed_days, total_days = tracker.get_habit_progress(habit)
        if total_days > 0:
            progress = (completed_days / total_days) * 100
            st.write(f"Habit: {habit}")
            st.write(f"Completed Days: {completed_days}")
            st.write(f"Total Days: {total_days}")
            st.write(f"Progress: {progress:.2f}%")
        else:
            st.write(f"No data found for habit '{habit}'.")
