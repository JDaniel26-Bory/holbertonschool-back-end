#!/usr/bin/python3
"""Import Modules"""
import requests
from sys import argv


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"

    user_id = argv[1]
    response = requests.get("{}users/{}/todos".format(URL, user_id),
                            params={"_expand": "user"})

    if response.status_code == 200:
        data = response.json()
        name = data[0]["user"]["name"]
        completed_task = [task for task in data if task["completed"]]

        print("Employee {} is done with tasks({}/{}):".format(
            name, len(completed_task), len(data)))
        for task in completed_task:
            print("\t {}".format(task["title"]))

    else:
        print("Error: {}".format(response.status_code))
