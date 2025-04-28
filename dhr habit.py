import json
import os
from datetime import datetime

DATA_FILE = "habits.json"

def load_habits():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        return {}

def save_habits(habits):
    with open(DATA_FILE, "w") as f:
        json.dump(habits, f, indent=4)

def add_habit(habits):
    name = input("Enter the name of the habit you want to track: ").strip()
    if name in habits:
        print("Habit already exists!")
    else:
        habits[name] = {"streak": 0, "last_done": None}
        print(f"Habit '{name}' added.")

def mark_done(habits):
    name = input("Enter the name of the habit you completed today: ").strip()
    if name not in habits:
        print("Habit not found.")
        return
    
    today = datetime.now().strftime("%Y-%m-%d")
    last_done = habits[name]["last_done"]
    
    if last_done == today:
        print("You already marked this habit done today!")
    else:
        if last_done == (datetime.now().replace(day=datetime.now().day - 1).strftime("%Y-%m-%d")):
            habits[name]["streak"] += 1
        else:
            habits[name]["streak"] = 1 
        habits[name]["last_done"] = today
        print(f"Habit '{name}' marked as done! Current streak: {habits[name]['streak']}")

def view_habits(habits):
    if not habits:
        print("No habits yet. Add one!")
        return
    print("\nYour Habits:")
    for name, data in habits.items():
        print(f"- {name}: Streak {data['streak']} days (last done: {data['last_done']})")
    print()

def main():
    habits = load_habits()

    while True:
        print("\nHabit Tracker Menu:")
        print("1. Add Habit")
        print("2. Mark Habit as Done")
        print("3. View Habits")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            add_habit(habits)
            save_habits(habits)
        elif choice == "2":
            mark_done(habits)
            save_habits(habits)
        elif choice == "3":
            view_habits(habits)
        elif choice == "4":
            save_habits(habits)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
