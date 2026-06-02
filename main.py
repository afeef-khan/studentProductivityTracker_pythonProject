# Welcome message to be displayed when program starts
def welcome_message():
    print(f"{60*"*"}")
    print(f"{8*"*"}  Welcome to StudentProductivityTracker  {11*"*"}")
    print(f"{60*"*"}")


# Selection menu from which user will select
def selection_menu():
    print(f"Select from the options below:")
    print("1) Add Task")
    print("2) View Task")
    print("3) Exit \n")
    user_choice = input("Enter Your Choice : ")
    return user_choice


# Add task function
def add_task():
    print("Add Task Loaded")


# View Task Function
def view_task():
    print("View Task Loaded")

# just a function to declare to make terminal results
def section_divider():
    print(40 * "=")


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
        add_task()
    elif user_choice == "2":
        view_task()
    elif user_choice == "3":
        print("Program Closed")
    elif "A" <= user_choice <= "Z" or "a" <= user_choice <= "z":
        print("Invalide Choice")
    else:
        print("Invalid Choice")
