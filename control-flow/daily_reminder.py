task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = "Invalid priority entered."

# Modify the reminder if the task is time-bound
if time_bound == "yes" and priority == "high":
    reminder += " It requires immediate attention today!"
elif time_bound == "yes":
    reminder += " It has a deadline, so plan accordingly."

print(reminder)