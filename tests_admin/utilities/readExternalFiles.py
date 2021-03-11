import json


class readFiles():
    @staticmethod
    def create_role_body():
        file = open("./tests_admin/testCases/create_role_body.json", 'r')
        body = json.loads(file.read())
        return body

    @staticmethod
    def create_user_body():
        file = open("./tests_admin/testCases/create_user_api.json", 'r')
        body = json.loads(file.read())
        return body

    @staticmethod
    def update_role_api():
        file = open("./tests_admin/testCases/update_role_api.json", 'r')
        body = json.loads(file.read())
        return body

    @staticmethod
    def update_user_api():
        file = open("./tests_admin/testCases/create_role_body.json", 'r')
        body = json.loads(file.read())
        return body


