#!/usr/bin/python3
"""Import Modules"""
from sys import argv
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"missing employee id as argument")
        sys.exit(1)

    URL = "https://jsonplaceholder.typicode.com/"

    EMPLOYEE_ID = argv[1]
    EMPLOYEE_TODOS = requests.get("{}users/{}/todos".format(URL, EMPLOYEE_ID),
                                  params={"_expand": "user"})

    data = EMPLOYEE_TODOS.json()
    EMPLOYEE_NAME = data[0]["user"]["name"]
    TOTAL_NUMBER_OF_TASKS = len(data)
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    for task in data:
        if task["completed"]:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(task["title"])
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for title in TASK_TITLE:
        print("\t ", title)
