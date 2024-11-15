
tasks = []

# greet user
def greet():
    print(f"Hello, {name.strip().title()}!")
    return name

#add a to do list entry
def add_task(task):
    tasks.append(task)
    print("Yet another thing to get done!")

# user input to add a task
def input_task():
    return input("Add a to do task: ")

#remove a to do list entry
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("One less burden!!")
    else:
        print("Nothing was removed...")

# user input for removal of a task
def remove_what():
    return input("Enter the task you accomplished: ").lower().strip()

# displays the task list in a formatted view
def view_list():
    if tasks:
        print(f"This is {name.title()}'s to do list:")
        for number, task in enumerate(tasks, start=1):
            print(f"{number}: {task}")
    else:
        print("Get a life already!")

# user navigation
def menu():
    return input("Enter A to add or R to remove a task, V to view your task list, Q to quit this application: ").strip().lower()

# This function gives the user the ability to navigate the application using the above options

def navigation():
    nav = True
    while nav == True:
        choice = menu()
        if choice == 'a':
            task = input_task()
            add_task(task)
        elif choice == 'r':
            task = remove_what()
            remove_task(task)
        elif choice == 'v':
            view_list()
        elif choice == 'q':
            print(f"See you later, {name.title()}!")
            nav = False
        else:
            print("That is not an option.")

# Start application by getting user's name
name = input("Enter your name: ")
greet()

navigation()

# application quits when user inputs Q, case and whitespace insensitive



