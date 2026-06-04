# Welcome message to be displayed when program starts
def welcome_message():
    print(f"{60*"*"}")
    print(f"{8*"*"}  Welcome to StudentProductivityTracker  {11*"*"}")
    print(f"{60*"*"}")


# just a function to declare to make terminal results readable
def section_divider():
    print(40 * "=")


# Selection menu from which user will select
def selection_menu():
    section_divider()
    print(f"Select from the options below:")
    print("1) Add Task")
    print("2) View Task")
    print("3) Exit")
    print("4) Delete Task \n")
    user_choice = input("Enter Your Choice : ")
    section_divider()
    return user_choice


task_list = []  # To store tasks added


# Add task function
def add_task():
    print("Add Task Loaded")
    section_divider()
    task_item = input("Enter Task name : ")
    section_divider()
    task_list.append(task_item)
    return task_item


# View Task Function
def view_task():
    print("View Task Loaded")
    section_divider()
    counter = 1
    if task_list == []:
        print("No Task Added yet!")
    else:
        for i in task_list:
            print(f"{counter}) {i}")
            counter = counter + 1


def delete_task():
    section_divider()
    if task_list == []:
        print("No Task Added yet!")
    else:
        print("To delete a task-")
        delete_input = int(input("Enter task no. you want to delete : "))
        to_delete = delete_input - 1
        if delete_input > len(task_list) or delete_input <= 0:
            section_divider()
            print("Invalid Task no.")
        else:
            del task_list[to_delete]
            section_divider()
            print("Task deletion successful")


# To print selection menu and storing value of user selection
def app():
    user_selection = selection_menu()
    return user_selection


# Variable made to store user choice
user_choice = 0

# Printing Welcome message before starting program
welcome_message()

# To iterate untill the user doesn't select 3
while user_choice != "3":

    # Calling app function and storing value of returned user_selection in user_choice variable
    user_choice = app()

    # To print user's
    section_divider()
    print(f"{"-" * 10} Your choice is {user_choice} {"-" * 12}")
    section_divider()

    # To check and call functions as per user's selection
    if user_choice == "1":
        task_item = add_task()
        print(f"Task Added = {task_item}\n")
    elif user_choice == "2":
        view_task()
    elif user_choice == "3":
        print("Program Closed")
    elif user_choice == "4":
        delete_task()
    else:
        print("Invalid Choice")
