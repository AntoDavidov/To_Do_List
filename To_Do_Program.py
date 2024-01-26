def show_menu():
    print('\n ----To-Do List Menu----')
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View Tasks")
    print("4. Quit")

def add_task(todo_list):
    task = input("Enter task: ")
    todo_list.append({"Task" : task, "Completed" : False})
    print(f"Task {task} added successfully!")


def mark_as_completed(todo_list):
    view_tasks(todo_list)
    index = int(input("Enter the index of a task to mark as completed: "))

    if 0 <= index < len(todo_list):
        todo_list[index]["Completed"] = True
        print("Task marked as completed successfully!")
    else:
        print("Invalid index. Please enter a valid one!")

def view_tasks(todo_list):
    print("----Tasks----")
    for i, task in enumerate(todo_list):
        status = "[X]" if task ["Completed"] else "[ ]"
        print(f"{i}. {status} {task}")


def to_do_list_program():
    todo_list = []

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            mark_as_completed(todo_list)
        elif choice == "3":
            view_tasks(todo_list)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please input a number between 1 and 4!")
            continue

to_do_list_program()