import os

tasks = []

#function to display tasks
def display_task(tasks):
    clear_screen()
    if not tasks:
        print("No tasks to display.")
    else:
        print("Tasks:")
        print("    ------------------------------")
        for task_id, task in enumerate(tasks, start=1):
            status = "Complete" if task['complete'] else "Incomplete"
            print(f"    Task ID     : {task_id}\n    Title       : {task['title']}\n    Description : {task['description']}\n    Status      : {status}")
            print("    ------------------------------")
    input("Press Enter to continue...")  


# Function to add tasks
def add_tasks(title, description):
    tasks.append({'title': title, 'description': description, 'complete': False})
    print(f"-->Task added.")
    input("Press Enter to continue...")  
    

# Function to mark task status
def task_status(tasks, task_id):
    if 1 <= task_id <= len(tasks):
        tasks[task_id - 1]['complete'] = not tasks[task_id - 1]['complete']
        status = "Complete" if tasks[task_id - 1]['complete'] else "Incomplete"
        print(f"-->Task {task_id} marked as {status}.")
    else:
        print(f"-->Task {task_id} not found.")
    input("Press Enter to continue...")  

# Function to delete task
def delete_task(tasks, task_id):
    if 1 <= task_id <= len(tasks):
        del tasks[task_id - 1]
        print(f"Task {task_id} deleted.")
        # Reassign task IDs after deletion
        for i, task in enumerate(tasks, start=1):
            task['id'] = i
    else:
        print("Invalid task ID.")
    input("Press Enter to continue...")  

# Function to save tasks to a file
def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        for task_id, task in enumerate(tasks, start=1):
            file.write(f"{task_id},{task['title']},{task['description']},{task['complete']}\n")
    print("-->Tasks saved to file.")
    input("Press Enter to continue...")  
    

# Function to fetch tasks from a file
def fetch_tasks(filename):
    tasks.clear()
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                task_id, title, description, complete = line.strip().split(',')
                tasks.append({'title': title, 'description': description, 'complete': complete == 'True'})
    return tasks

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main function
def main():
    global tasks
    tasks = fetch_tasks("tasks.txt")

    while True:
        clear_screen()
        print("\n--------------------------------------")
        print("To-Do List Application")
        print("--------------------------------------")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete OR Incomplete")
        print("4. Save Tasks")
        print("5. Delete Task")
        print("6. Exit")
        print("--------------------------------------")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("--------------------------------------")
            title = input("Enter task Title: ")
            description = input("Enter task description: ")
            print("--------------------------------------")
            add_tasks(title, description)

        elif choice == '2':
            display_task(tasks)

        elif choice == '3':
            task_id = int(input("Enter task ID: "))
            task_status(tasks, task_id)

        elif choice == '4':
            save_tasks(tasks, "tasks.txt")

        elif choice == '5':
            task_id = int(input("Enter task ID: "))
            delete_task(tasks, task_id)

        elif choice == '6':
            save_tasks(tasks, "tasks.txt")
            print("Bye bye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
