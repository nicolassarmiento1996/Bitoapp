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
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

if __name__ == '__main__':
    tracker = HabitTracker()

    while True:
        print("\nHabit Tracker")
        print("1. Add Habit")
        print("2. Remove Habit")
        print("3. Check Off Habit")
        print("4. View Habits")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            habit = input("Enter the habit to add: ")
            tracker.add_habit(habit)
        elif choice == '2':
            habit = input("Enter the habit to remove: ")
            tracker.remove_habit(habit)
        elif choice == '3':
            habit = input("Enter the habit to check off: ")
            tracker.check_off_habit(habit)
        elif choice == '4':
            tracker.view_habits()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
