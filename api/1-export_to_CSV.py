#!/usr/bin/python3
"""Gathering the needed informations from the API."""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    user_id = argv[1]
    response = requests.get(
        f'{url}/users/{user_id}/todos',
        params={'_expand': 'user'}
    )

    data = response.json()
    name = data[0]['user']['name']
    fileName = f"{user_id}.csv"

    with open(fileName, "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for task in data:
            writer.writerow(
                [user_id, name, str(task["completed"]),
                 task["title"]]
            )
