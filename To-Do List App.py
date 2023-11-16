# To-Do List App in Python

# Initialize an empty list to store tasks
tasks = []

# Function to add a task
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added: ", task)

# Function to list tasks
def list_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

# Function to mark a task as complete
def mark_complete():
    list_tasks()
    task_number = int(input("Enter the task number to mark as complete: "))
    if 1 <= task_number <= len(tasks):
        task = tasks[task_number - 1]
        print(f"Task marked as complete: {task}")
        tasks.remove(task)
    else:
        print("Invalid task number.")

# Main loop
while True:
    print("\nMenu:")
    print("1. Add a task")
    print("2. List tasks")
    print("3. Mark a task as complete")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        mark_complete()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please select a valid option.")