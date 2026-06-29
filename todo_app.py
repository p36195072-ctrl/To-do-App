import json

# Load data
try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = {}


def add_task():
    task = input("Enter Task: ")

    if task.strip() == "":
        print("Task cannot be empty!")
        return

    if task in tasks:
        print("Task already exists!")
        return

    tasks[task] = {
        "status": "Pending"
    }

    print("Task Added Successfully!")


def view_tasks():
    if len(tasks) == 0:
        print("No Tasks Found")
        return

    print("\n===== TASK LIST =====")
    for task, details in tasks.items():
        print(f"Task   : {task}")
        print(f"Status : {details['status']}")
        print("-" * 25)


while True:
    print("\n===== TO DO APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)

        print("Tasks Saved Successfully!")
        print("Goodbye!")
        break

    else:
        print("Invalid Choice! Please try again.")
