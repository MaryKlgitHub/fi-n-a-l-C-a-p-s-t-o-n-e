# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VSC ode otherwise the
# program will look in your root directory for the text files.
#=====importing libraries===========
import os
from datetime import datetime, date

# Initialize empty dictionary, string, list, the file respectively to store data 
username_password = {}
current_user = ""
DATETIME_STRING_FORMAT = "%Y-%m-%d"
task_list = []
tasks_file = "tasks.txt"

# Block code for adding a new task (when user selects 'a' option im menu). 
def add_task():
    # Prompt for the username of the person assigned to the task
    # Check if the username exists in the username_password dictionary
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username.")
        return
    # Prompt for the title of the task, try except block to handle empty title
    while True:
        task_title = input("Title of Task: ")
        if not task_title.strip():
            print("Title cannot be empty. Please try again.")
        else:
            break
    # Prompt for the description of the task, user is able to skip it by pressing Enter
    task_description = input("Description of Task (Press Enter to skip): ")
    # Prompt for the due date og the task and validate the datetime format
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")
    # Get the current date and create a new task dictionary with the provided details
    # Add the new task to the task_list
    current_date = date.today()
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": current_date,
        "completed": False
    }
    task_list.append(new_task)
    save_task_list() # Save the updated task_list
    print("Task successfully added.") # Print out a sucess message

# Helper function to get integer from the user
def get_integer(message):
    returnNumber = input(message)    
    while True:
        try:
            int(returnNumber)
            return int(returnNumber)
        except ValueError:
            returnNumber = input("Please enter a number: ")

# Block code for saving the task_list to a file
def save_task_list():
    # Open the file in a write mode, using a 'with'statement to ensure proper file handling
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for task in task_list:
            string_attributes = [
                task['username'],
                task['title'],
                task['description'],
                task['due_date'].strftime(DATETIME_STRING_FORMAT),
                task['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if task['completed'] else "No"
            ]
            task_list_to_write.append(";".join(string_attributes))
        task_file.write("\n".join(task_list_to_write)) # Write the contents of task_list_to_write to the file

# Code block to implement a user login system by reading username-password from a file
# Promting the user for their credentials and validating them against the stored data
def user_login():
    if not os.path.exists("user.txt"):
        with open("user.txt", "w") as default_file:
            default_file.write("admin;password")
    # Read in user_data
    with open("user.txt", 'r') as user_file:
        user_data = user_file.read().split("\n")
    # Convert to a dictionary
    for user in user_data:
        username, password = user.split(';')
        username_password[username] = password

    logged_in = False
    global current_user
    while not logged_in:
        print("LOGIN")
        current_user = input("Username: ")
        curr_pass = input("Password: ")
        # Check if the entered username exists in the dictionary
        if current_user not in username_password.keys():
            print("User does not exist. Please enter a valid username.")
            continue
        # Check if the entered password matches the stored password for the username
        elif username_password[current_user] != curr_pass:
            print("Wrong password")
            continue
        else:
            print("Login Successful!")
            logged_in = True

# Code block to perform checks for adding a new user, including ensuring the password
# Confirm password match and check if the username already exists
def reg_user():
    while True:
        new_username =     input("New Username: ")
        new_password =     input("New Password: ")
        confirm_password = input("Confirm Password: ")
        if new_password == confirm_password:
            if new_username in username_password:
                # Check if the username already exists
                print("User is already exist. Please use another name.")
                continue
            # Add the new user and save the user data
            print("New user added.")
            username_password[new_username] = new_password
            with open("user.txt", "w") as out_file:
                user_data = []
                for name in username_password:
                    user_data.append(f"{name};{username_password[name]}")
                out_file.write("\n".join(user_data))
                return
        else:
            print("Passwords do no match.") #Passwords do not match, prompt again

# Defininf the function 'view_all()' that reads the task list from task.txt file
# Prints out all the tasks to the console in the specific format
def view_all():
    print()
    print("------------View All Tasks--------------------")
    # Iterating through the task list
    n = 1
    for task in task_list:
        print("\nTask#", n)
        n += 1
        # Construct the display string with task details
        display_string =  f"Task: \t\t {task['title']}\n"
        display_string += f"Assigned to: \t {task['username']}\n"
        display_string += f"Date Assigned: \t {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        display_string += f"Due Date: \t {task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        display_string += f"Task Complete? \t {'Yes'if task['completed'] else 'No'}\n"
        display_string += f"Task Description: \n {task['description']}\n"
        print(display_string)
    print("----------------------------------------------")

# Defining the function view_mine() to read the tasks assigned to the current user
def view_mine():
    print()
    print("----------------My Tasks---------------------")
    n = 1
    for task in task_list:
        if task['username'] == current_user:
            print("\nTask #", n) # Printing out the task number
            n += 1
            display_string =  f"Task: \t\t{task['title']}\n"
            display_string += f"Assigned to: \t{task['username']}\n"
            display_string += f"Date Assigned: \t{task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            display_string += f"Due Date: \t{task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            display_string += f"Task Complete? \t {'Yes'if task['completed'] else 'No'}\n"
            display_string += f"Task Description: \n{task['description']}\n"
            print(display_string) # Printing the task details
    print("---------------------------------------------")
    select_specific_task() # Call function to select a specific task

# Defining 'select_specific_task' func that allows the user to choose a specific task by entering a number
# If a valid task number it calls 'edit_specific_task'func to modify the task
def select_specific_task():
    print("Select a specific task (by entering a number) or input ‘-1’ to return to the main menu")
    task_number = get_integer(": ") 
    if task_number == "-1": # Option to return to the main menu
        return
    else:
        print("You choose task number:", task_number)
        n = 1
        for task in task_list:
            if task['username'] == current_user: # Check if the current task number mathes the user's input
                if n == int(task_number):
                    edit_specific_task(task) # Call the function to edit the specific task
                    return
                n += 1
        # If not matching task is found, display an error message
        print("Task with number", task_number, "does not exist. Try again.")

# Define the func 'edic_specific_task that allows the user select an action for a specific task
# Such as marking it as complete or editing the details.
def edit_specific_task(task):
    print(task['title'])
    while True:
        print("m - Mark the task as complete")
        print("e - Edit the task")
        # Read the user's input and convert it to lowercase
        m = input(": ").lower()
        # Define a dictionary of options for the user's input
        m_options = {
            'm': mark_task_as_complete,
            'e': edit_task,
        }
        # Check if the user's input is a valid option
        if m in m_options:
            # Call the corresponding function based on the user's input
            m_options[m](task)
            return
        else:
            print("You have made a wrong choice. Please try again.")

# Defining a function 'mark_task_as_complete'that updates the completion status of a task to True
# Printing out the confirmation message
# Save the updated task list to file
def mark_task_as_complete(task):
    task['completed'] = True
    print("Task Completed")
    save_task_list()

# Define the function 'edit_task'that allows the user to edit the assigned user and due data of a task, provided that the task has not been completed.
# Perform input validation and update the task, save the updated task list to a file
def edit_task(task):
    if task['completed'] == True:
        print("The task has already been completed")
    else:
        print("Edit the task:", task['title'])
        new_username = input("Please type new User Name : ").lower()
        if new_username not in username_password: # Check if the user exists in the user database
            print("The user doesn't exist. Please use existing user name.")
        else:
            task['username'] = new_username

        due_date = input("Please type new Due Date: ").lower()
        due_date = datetime.strptime(due_date, DATETIME_STRING_FORMAT)
        task['due_date'] = due_date
        save_task_list()

# Block code to define the function 'display_statistics' to print statistics from files user and text overview
# To check first if the current user is an admin
def display_statistics():
    print()
    if current_user != 'admin':
        print("You do not have permission to access this option.")
        return
    # call the function generate reports if file don't exist
    if not os.path.isfile("user_overview.txt") or not os.path.isfile("task_overview.txt"):
        generate_reports()
    # Display the content of user_overview.txt
    print("\nUser Overview Report:")
    with open("user_overview.txt", "r") as user_overview_file:
        print(user_overview_file.read())
    # Display the content of task_overview.txt
    print("\nTask Overview Report:")
    with open("task_overview.txt", "r") as task_overview_file:
        print(task_overview_file.read())

# Define the func 'exit' that prints out the final message and calls the func to terminate the program execution
def exit_menu():
    print()
    print('Goodbye!!!')
    exit()

# Define the function 'read_tasks' to read task data from a file, to parse it and create task dictionaries based on the components
# Handle the file existence check, read and split data
def read_tasks():
    if not os.path.exists(tasks_file):
        with open(tasks_file, "w") as default_file:
            pass
    with open(tasks_file, 'r') as task_file:
        task_data = task_file.read().split("\n")
        task_data = [t for t in task_data if t != ""]

    for task_string in task_data:
        current_task = {}
        # Split by semicolon and manually add each component
        task_components = task_string.split(";")
        current_task['username'] = task_components[0]
        current_task['title'] = task_components[1]
        current_task['description'] = task_components[2]
        current_task['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
        current_task['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
        current_task['completed'] = True if task_components[5] == "Yes" else False
        task_list.append(current_task)
    return task_list

# Define a function 'generate reports' that allows to generate 2 reports: a user overview and a task overview.
# To save generated reports in separated text files. 
def generate_reports():
    print("Generating Reports...") # Print out the message to indicate that the reports are being generated
    user_overview = "user_overview.txt"
    # Get the total number of users and tasks
    users_total_number = str(len(username_password))
    tasks_total_number= sum(len([task for task in task_list if task['username'] == username]) for username in username_password)
    # Generate user overview report and write the attributes for user overview
    with open(user_overview, "w") as user_overview_file:
        string_attributes = [
            "Users total number: " + users_total_number,
            "Tasks total number: " + str(tasks_total_number),
        ]
        user_overview_file.write("\n".join(string_attributes))
        #For each user describe statistics
        for username in username_password:
            user_tasks = [task for task in task_list if task['username'] == username]
            total_tasks = len(user_tasks)
            percentage_total_tasks = (total_tasks/tasks_total_number) * 100
            completed_tasks = sum(task['completed'] for task in user_tasks)
            percentage_completed_tasks = (completed_tasks/total_tasks) * 100 if total_tasks > 0 else 0
            incomplete_tasks = total_tasks - completed_tasks
            percentage_incomplete_tasks = (incomplete_tasks/total_tasks) * 100 if total_tasks > 0 else 0
            overdue_tasks = sum(task ['due_date'] > datetime.now() and not task ['completed'] for task in user_tasks)
            percentage_overdue_tasks = (overdue_tasks / total_tasks) * 100 if total_tasks > 0 else 0
            # Write the statistics to the user overview file
            user_overview_file.write("\n\nUser: " + username)
            user_overview_file.write("\n" + "-" * 50)  # Add a straight line
            user_overview_file.write("\nStatistics:")
            user_overview_file.write("\nTotal tasks assigned: " + str(total_tasks))
            user_overview_file.write("\nPercentage of total tasks assigned: {:.2f}%".format(percentage_total_tasks))
            user_overview_file.write("\nPercentage of completed tasks: {:.2f}%".format(percentage_completed_tasks))
            user_overview_file.write("\nPercentage of incomplete tasks: {:.2f}%".format(percentage_incomplete_tasks))
            user_overview_file.write("\nPercentage of overdue tasks: {:.2f}%".format(percentage_overdue_tasks))

    # File name for task overview report
    task_overview = "task_overview.txt"
    # Initialize variables for task statistics
    completed_tasks = sum(task['completed'] for task in task_list)
    incomplete_tasks = int(tasks_total_number) - completed_tasks
    incomplete_overdue = sum(task['due_date'] > datetime.now() and not task['completed'] for task in task_list)
    incomplete_percentage = (incomplete_tasks/int(tasks_total_number)) * 100
    overdue_percentage = (incomplete_overdue / int(tasks_total_number)) * 100
    # Generate task overview report
    with open(task_overview, "w") as task_overview_file:
        task_overview_file.write("Tasks total number: " + str(tasks_total_number) + "\n")
        task_overview_file.write("Completed tasks total number: " + str(completed_tasks) + "\n")
        task_overview_file.write("Incomplete tasks total number: " + str(incomplete_tasks) + "\n")
        task_overview_file.write("Incomplete tasks overdue: " + str(incomplete_overdue) + "\n")
        task_overview_file.write("Incomplete tasks percentage: {:.2f}%\n".format(incomplete_percentage))
        task_overview_file.write("Overdue tasks percentage: {:.2f}%\n".format(overdue_percentage))
    # Print a message to indicate that the reports have been generated successfully.
    print("Reports successfully generated.")

# The code block represents the main task processing loop of the program. 
# Present a menu to the user and handles their input based on the selected option.
def tasks_processing():
    while True:
        # presenting the menu to the user and
        # making sure that the user input is converted to lower case.
        print()
        print("Please select one of the following options:")
        print("r - Registering a user")
        print("a - Adding a task")
        print("va - View all tasks")
        print("vm - View my tasks")
        print("gr - Generate Reports")
        print("ds - Display statistics")
        print("e - Exit")
        menu = input(": ").lower()
        # Menu options available to the user and the corresponding actions performed for each option
        menu_options = {
            'r': reg_user,
            'a': add_task,
            'va': view_all,
            'vm': view_mine,
            'gr': generate_reports,
            'ds': display_statistics,
            'e': exit_menu,
        }

        if menu in menu_options:
            menu_options[menu]() # Execute the selected function based on user's input.
        else:
            print("You have made a wrong choice. Please try again.")


# Perform user login, read tasks from a file and enter the main processing loop
if __name__ == "__main__":
    user_login()
    read_tasks()
    tasks_processing()