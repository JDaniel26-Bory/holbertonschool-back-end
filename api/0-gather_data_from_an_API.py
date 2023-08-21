#!/usr/bin/python3
"""Import Modules"""
import requests
from sys import argv


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"

    EMPLOYEE_ID = argv[1]
    EMPLOYEE_TODOS = requests.get("{}users/{}/todos".format(URL, EMPLOYEE_ID),
                                  params={"_expand": "user"})

    if EMPLOYEE_TODOS.status_code == 200:
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
    else:
        print("Error: {}".format(EMPLOYEE_TODOS.status_code))
