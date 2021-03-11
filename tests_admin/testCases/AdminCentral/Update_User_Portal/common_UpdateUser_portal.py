import json

import requests
from xeger import Xeger

from tests_admin.utilities.readProperties import ReadConfig

class common_createUser_portal():
    def headers(self):
        url = ReadConfig.sm()
        headers = {'Content-Type': 'application/json'}
        a = {"userName": "CMUIServer", "password": "a5a78cfc0e4711ebadc10242ac120002"}
        resp = requests.post(url + '/getSMToken', headers=headers, data=json.dumps(a, indent=4))
        token=resp.text
        # print("\nTotal token::\n", token)
        d = json.loads(token)
        message=d["status_message"]
        e = json.loads(message)
        accesstoken = "Bearer "+e["accessToken"]
        # print("\n AccessToken   :::\n", accesstoken)
        headers = {'Content-Type': 'application/json', 'Authorization': accesstoken}
        return headers

    def verify_user_in_sm(self):
        url = ReadConfig.sm()
        headers = {'Content-Type': 'application/json'}
        a = {"userName": "CMUIServer", "password": "a5a78cfc0e4711ebadc10242ac120002"}
        resp = requests.post(url + '/getSMToken', headers=headers, data=json.dumps(a, indent=4))
        token = resp.text
        d = json.loads(token)
        message = d["status_message"]
        e = json.loads(message)
        accesstoken = "Bearer " + e["accessToken"]
        headerss = {'Content-Type': 'application/json', 'Authorization': accesstoken}
        r = requests.get(url + "/getUsers", headers=headerss)
        # print("Data from SM::\n", r.json())
        # extracting data in json format
        list = []
        for item in r.json():
            usernames = item.get('userName')
            list.append(usernames)
        print("Users are :::\n", list)
        return list

    def verify_user_details_sm(self):
        url = ReadConfig.sm()
        headers = {'Content-Type': 'application/json'}
        a = {"userName": "CMUIServer", "password": "a5a78cfc0e4711ebadc10242ac120002"}
        resp = requests.post(url + '/getSMToken', headers=headers, data=json.dumps(a, indent=4))
        token = resp.text
        d = json.loads(token)
        message = d["status_message"]
        e = json.loads(message)
        accesstoken = "Bearer " + e["accessToken"]
        headerss = {'Content-Type': 'application/json', 'Authorization': accesstoken}
        r = requests.get(url + "/getUsers", headers=headerss)
        # print("Data from SM::\n", r.json())
        # extracting data in json format
        list = []
        for item in r.json():
            usernames = item.get('userName')
            list.append(usernames)
        print("Users are :::\n", list)
        return list





