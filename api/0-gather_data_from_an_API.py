#!/usr/bin/python3
"""Import Modules"""
import requests
import sys
from sys import argv


if __name__ == "__main__":

    EMPLOYEE_ID = argv[1]
    response_users = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(EMPLOYEE_ID))
    response_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(EMPLOYEE_ID))

    if response_users.status_code != 200 or response_todos.status_code != 200:
        print("Error: {}".format(
            response_users.status_code or response_todos.status_code))
        sys.exit(1)

    user_data = response_users.json()
    todos_data = response_todos.json()

    employee_name = user_data.get('name')
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    print("Employee {} is done with tasks({}/{})".format(
        employee_name, completed_tasks, total_tasks))

    for todo in todos_data:
        if todo['completed']:
            print(f"\t{todo['title']}")
