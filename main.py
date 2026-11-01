
import json


tasks = []



def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []



def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)



def add_task():
    task = input("Enter your task: ").strip()

    if task:
        new_task = {
            "title": task,
            "completed": False
        }

        tasks.append(new_task)
        save_tasks()

        print("Task added successfully!")

    else:
        print("Task cannot be empty!")


def view_tasks():
    if not tasks:
        print("No tasks found!")

    else:
        print("\nYour Tasks:")

        for index, task in enumerate(tasks, start=1):

            if task["completed"]:
                status = "Completed"
            else:
                status = "Pending"

            print(f"{index}. {task['title']} - {status}")


def complete_task():
    if not tasks:
        print("No tasks available!")
        return

    view_tasks()

    try:
        task_number = int(input("Enter task number to complete: "))

        if 1 <= task_number <= len(tasks):

            if tasks[task_number - 1]["completed"]:
                print("This task is already completed!")

            else:
                tasks[task_number - 1]["completed"] = True
                save_tasks()

                print("Task completed successfully!")

        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


def mark_pending():
    if not tasks:
        print("No tasks available!")
        return

    view_tasks()

    try:
        task_number = int(input("Enter task number to mark as pending: "))

        if 1 <= task_number <= len(tasks):

            if tasks[task_number - 1]["completed"]:
                tasks[task_number - 1]["completed"] = False

                save_tasks()

                print("Task marked as pending!")

            else:
                print("This task is already pending!")

        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")



def delete_task():
    if not tasks:
        print("No tasks available to delete!")
        return

    view_tasks()

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):

            confirmation = input(
                "Are you sure you want to delete this task? (y/n): "
            ).lower()

            if confirmation == "y":
                deleted_task = tasks.pop(task_number - 1)
                save_tasks()

                print(f"'{deleted_task['title']}' deleted successfully!")

            else:
                print("Deletion cancelled!")

        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


def main():
    global tasks
    tasks = load_tasks()

    while True:
        print("\n========== TO-DO LIST ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Mark Task as Pending")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            mark_pending()
        
        
        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")



if __name__ == "__main__":
    main()



   
