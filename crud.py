import os

# Function to create a new task
def create_task(task_list, task):
    task_list.append(task)

# Function to read all tasks
def read_tasks(task_list):
    for index, task in enumerate(task_list):
        print(f"{index + 1}. {task}")

# Function to update a task
def update_task(task_list, index, new_task):
    if index >= 0 and index < len(task_list):
        task_list[index] = new_task
    else:
        print("Invalid task index")

# Function to delete a task
def delete_task(task_list, index):
    if index >= 0 and index < len(task_list):
        del task_list[index]
    else:
        print("Invalid task index")

# Function to save tasks to a text file
def save_tasks_to_file(task_list, filename):
    with open(filename, "w") as file:
        for task in task_list:
            file.write(task + "\n")

# Function to load tasks from a text file
def load_tasks_from_file(filename):
    task_list = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            task_list = file.read().splitlines()
    return task_list

# Main function
def main():
    filename = "tasks.txt"
    tasks = load_tasks_from_file(filename)

    while True:
        print("\nTask Management Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a new task: ")
            create_task(tasks, task)
        elif choice == "2":
            read_tasks(tasks)
        elif choice == "3":
            index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            update_task(tasks, index, new_task)
        elif choice == "4":
            index = int(input("Enter the task number to delete: ")) - 1
            delete_task(tasks, index)
        elif choice == "5":
            save_tasks_to_file(tasks, filename)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()