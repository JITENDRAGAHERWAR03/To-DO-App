tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(index):
    try:
        removed_task = tasks.pop(index - 1)
        print(f"Task '{removed_task}' removed.")
    except IndexError:
        print("Invalid task number.")

print("Welcome to the To-Do App!")
while True:
    print("\nOptions:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_tasks()
        try:
            index = int(input("Enter the task number to remove: "))
            remove_task(index)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
