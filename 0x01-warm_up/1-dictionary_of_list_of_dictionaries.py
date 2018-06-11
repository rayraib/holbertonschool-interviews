#!/usr/bin/python3
''' make api call to get employee info'''
import json
import requests


def make_apicall():
    ''' make get request, and write the data to .json file'''
    userId = 1

    result = {}
 
    while (userId):
        info_value = []
        dict_val = {}
        url = "https://jsonplaceholder.typicode.com/todos?userId=" + str(userId)
        r = requests.get(url)
        r = r.json()
        if len(r) == 0:
            break
        u_url = 'https://jsonplaceholder.typicode.com/users/' + str(userId)
        user_info = requests.get(u_url)
        username = (user_info.json())['username']
        for task in r:
            title = task["title"]
            completed = task["completed"]
            dict_val["username"] = username
            dict_val["task"] = title
            dict_val["completed"] = completed
            info_value.append(dict_val)
        result[str(userId)] = info_value
        userId += 1

    with open("todo_all_employees.json", 'w') as f:
        json.dump(result, f)


if __name__ == "__main__":
    make_apicall()
