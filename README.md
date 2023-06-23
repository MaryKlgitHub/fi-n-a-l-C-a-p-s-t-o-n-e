# FinalCapstone. The lists, functions, and string handling capstone project.

Welcome to my portfolio. This repository contains the code for the finalCapstone project for HyperionDev the bootcamp's software engineering foundations course.

## Project Overview

This project is a task management system implemented in Python. It allows users to create tasks, assign them to specific users, set due dates, and track their completion status. The program provides a command-line interface for interacting with the task management system. In this project I used lists or dictionaries and functions to extend the functionality of a simple task managment system. The project aims to acess my ability to refactor code. I reduced the code complexity of the previous code and ensured the readability of the functioning code.

## Instructions

1. Make sure you have Python installed on your local machine.
2. Clone this repository to your local machine.
3. Open the project folder in Visual Studio Code (VSC) or any other code editor of your choice.
4. Open the terminal or command prompt in the project folder.
5. Run the `task_manager.py` file using the Python interpreter.

## Usage

- Upon running the `task_manager.py` file, you will be prompted to enter your username and password to access the admin rights. Use the following credentials:
  - Username: admin
  - Password: password

- The program will look for the `tasks.txt` and `user.txt` files in the root directory. Make sure to open the entire project folder in VSC or the program will look in your root directory for the text files. If file don't exist, the program will create files.

- The program provides the following options:
  - `r`: Registering a user
  - `a`: Add a new task
  - `va`: View all tasks
  - `vm`: View my tasks
  - `gr`: Generate reports
  - `ds`: Display statistics (only accessible for the admin user)
  - `e`: Exit
    
### Some screenshots of the program below:

User overview report

<img width="750" alt="Screenshot 2023-06-23 at 14 51 52" src="https://github.com/MaryKlgitHub/fi-n-a-l-C-a-p-s-t-o-n-e/assets/126916883/c96a1584-1137-44da-a365-e07cb32bccdd">

menu 'vm'

<img width="750" alt="Mytask" src="https://github.com/MaryKlgitHub/fi-n-a-l-C-a-p-s-t-o-n-e/assets/126916883/2305acee-02b9-4b63-9d28-90100be65a6f">

Additional functionality in 'vm'

<img width="750" alt="Screenshot 2023-06-23 at 14 50 52" src="https://github.com/MaryKlgitHub/fi-n-a-l-C-a-p-s-t-o-n-e/assets/126916883/a5f72189-dddd-415c-944c-2b3d0560484a">

- Follow the on-screen instructions to perform the desired actions.

## Dependencies

This project relies on the following libraries:

- `os`: For file and directory operations
- `datetime`: For working with dates and times

Make sure to install these dependencies before running the program.

## Contributing

I welcome contributions from everyone! If you have any suggestions, improvements, or bug fixes, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

