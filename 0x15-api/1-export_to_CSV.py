#!/usr/bin/python3

import requests
import sys
import csv

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = f"{base_url}users/{employee_id}"
    todos_url = f"{base_url}todos"

    # Fetch user information
    user_response = requests.get(user_url)
    user = user_response.json()

    # Fetch user's TODO list
    todos_params = {"userId": employee_id}
    todos_response = requests.get(todos_url, params=todos_params)
    todos = todos_response.json()

    # Prepare CSV file name
    csv_file_name = f"{employee_id}.csv"

    # Write data to CSV file
    with open(csv_file_name, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write tasks
        for task in todos:
            writer.writerow({
                "USER_ID": user["id"],
                "USERNAME": user["username"],
                "TASK_COMPLETED_STATUS": str(task["completed"]),
                "TASK_TITLE": task["title"]
            })

    print(f"Data exported to {csv_file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

