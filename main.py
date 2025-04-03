import os
import json
from datetime import datetime

#Init
status = ["Todo", "In-progress", "Done"]
file_path = "tasksDB.json"

if not os.path.exists(file_path):
    with open(file_path, "w") as file:
        file.write("{}")
        print(f"{file_path} created successfully")
else:
    print(f"{file_path} already exists")

#--------
    
def save_to_file(tasks):
    with open(file_path, "w") as file:
        json.dump(tasks, file, indent=4)

def adding_task():
    user_tasks = str(input("Write task you want to track: "))
    current_time = datetime.now().strftime("%A %d/%m/%Y %H:%M:%S")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                tasks = {}
    else:
        tasks = {}
        
    if tasks:
        id = str(max(map(int, tasks.keys())) + 1)
    else:
        id = "1"
    
    tasks[id] = {
        "description": user_tasks,
        "status": "Todo",
        "createdAt": current_time,
        "updatedAt": current_time
    }
    with open(file_path, "w") as file:
        json.dump(tasks, file, indent=4)
    print("Task created!")

def view_tasks():
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                print("No task found.")
                return
    else:
        print("No tasks found.")
        return
    if not tasks:
        print("No tasks available.\n")
        return
    
    print("\n1. View all tasks")
    print("2. View 'Todo' tasks")
    print("3. View 'In-progress' tasks")
    print("4. View 'Done' tasks")
    user_choices = str(input("Select the options: "))
    if user_choices == "1":
        print("\nYour Tasks: ")
        for task_id, task_details in tasks.items():
            print(f"ID: {task_id}")
            print(f"Description: {task_details['description']}")
            print(f"Status: {task_details['status']}")
            print(f"Created At: {task_details['createdAt']}")
            print(f"Updated At: {task_details['updatedAt']}")
            print(" ")
    elif user_choices in ["2", "3", "4"]:
        selected_status = status[int(user_choices) - 2]
        print(f"\nYour '{selected_status}' Tasks: ")
        for task_id, task_details in tasks.items():
            if task_details["status"] == selected_status:
                print(f"ID: {task_id}")
                print(f"Description: {task_details['description']}")
                print(f"Status: {task_details['status']}")
                print(f"Created At: {task_details['createdAt']}")
                print(f"Updated At: {task_details['updatedAt']}")
                print(" ")
    else:
        print("Please select a valid option!\n")
        return

def delete_task():
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                print("No task found.")
                return
    else:
        print("No tasks found.")
        return
    
    if not tasks:
        print("No tasks available.\n")
        return
    print("\nYour Tasks: ")
    for task_id, task_details in tasks.items():
        print(f"ID: {task_id}")
        print(f"Description: {task_details['description']}")
        print(f"Status: {task_details['status']}")
        print(f"Created At: {task_details['createdAt']}")
        print(f"Updated At: {task_details['updatedAt']}")
        print(" ")
    user_choices = str(input("Select the ID of task you want to delete (Press 'q' to cancel): "))
    if user_choices in tasks:
        tasks.pop(user_choices)
        save_to_file(tasks)
        print("Task deleted!\n")
    elif user_choices == "q":
        return    
    else:
        print("There is no such task with that ID!")
        return

def update_task():
    current_time = datetime.now().strftime("%A %d/%m/%Y %H:%M:%S")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                print("No task found.")
    else:
        print("No tasks found.")
        return
    
    if not tasks:
        print("No tasks available.\n")
        return
    
    print("\nYour Tasks: ")
    for task_id, task_details in tasks.items():
        print(f"ID: {task_id}")
        print(f"Description: {task_details['description']}")
        print(f"Status: {task_details['status']}")
        print(f"Created At: {task_details['createdAt']}")
        print(f"Updated At: {task_details['updatedAt']}")
        print(" ")

    user_choices = str(input("Select the ID of task you want to update (Press 'q' to cancel): ")).lower()
    if user_choices in tasks:
        print("1. Edit or update task description")
        print("2. Update task status")
        update_selection = str(input("Select the options: "))
        if update_selection == "1":
            description = str(input("Write the new description: "))
            tasks[user_choices]["description"] = description
            tasks[user_choices]["updatedAt"] = current_time
            save_to_file(tasks)
            print("Task updated!\n")
            
        elif update_selection == "2":
            print("Status: ")
            print("1. Todo")
            print("2. In-progress")
            print("3. Done")
            status_select = str(input("Select status you want to update into: "))
            if status_select in ["1", "2", "3"]:
                tasks[user_choices]["status"] = status[int(status_select)-1]
                tasks[user_choices]["updatedAt"] = current_time
                save_to_file(tasks)
                print("Task updated!\n")
            else:
                print("Please choose the right options!")
        else:
            print("Please choose the right options!")
    elif user_choices == "q":
        return
    else:
        print("There is no such task with that ID!")
        return
    
while True:
    print("Welcome to task tracker!")
    print("1. Add new task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Update a task")
    user_selection = str(input("What are you going to do? (Press 'q' to exit): ")).lower()
    if user_selection == "1":
        adding_task()
    elif user_selection == "2":
        view_tasks()
    elif user_selection == "3":
        delete_task()
    elif user_selection == "4":
        update_task()
    elif user_selection == "q":
        print("Thank you! See you later!")
        break
    else:
        print("Please select the right options!")

