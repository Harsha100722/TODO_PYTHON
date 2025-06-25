def _menu():
    print("\n--- To-Do List Menu ---")
    print("1. show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def load_tasks():
    try:
        with open("Tasks_List.txt", "r") as file:
            tasks = file.read().splitlines()
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("Tasks_List.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added succssfully..!")

def remove_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter the task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Removed successfully..!: {removed}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a number.")

tasks = load_tasks()

while True:
    _menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        show_tasks(tasks)
    elif choice == "2":
        add_task(tasks)
    elif choice == "3":
        remove_task(tasks)
    elif choice == "4":
        save_tasks(tasks)
        print("Tasks saved. Goodbye!")
        break
    else:
        print("Please choose a valid option.")
