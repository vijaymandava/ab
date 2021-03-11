import json
import random
import string
from datetime import date
from xeger import Xeger

from tests_admin.utilities.readProperties import ReadConfig


class username_field_validations():

    # UserName
    def username_regex(self):
        x = Xeger(limit=34)
        regex = ReadConfig.userName_RegEx()
        name = regex
        username = x.xeger(name)
        print("\n Trying to create user :::", username)
        return username

    def username_single_character(self):
        x = Xeger(limit=34)

        regex = ReadConfig.userName_RegEx()
        name = regex
        role = x.xeger(name)

        def randStr(chars=role, N=8):
            return ''.join(random.choice(chars) for _ in range(N))

        username = randStr(N=1)
        print("\n Trying to create user", username)
        return username

    def username_max_characters(self):
        def randStr(chars=string.ascii_uppercase + string.ascii_lowercase, N=8):
            return ''.join(random.choice(chars) for _ in range(N))

        username = randStr(N=50)
        print("\n Trying to create user :::", username)
        return username

    def username_max_plus_one(self):
        def randStr(chars=string.ascii_uppercase + string.ascii_lowercase, N=8):
            return ''.join(random.choice(chars) for _ in range(N))

        username = randStr(N=51)
        print("\n Trying to create user ::", username)
        return username

    def username_spaces_inbetween(self):
        def randStr(chars=string.ascii_uppercase + ' ' + ' ', N=8):
            return ''.join(random.choice(chars) for _ in range(N))

        username = randStr(N=10)
        print("\n Trying to create user :::", username)
        return username

    def username_uppercase(self):
        def randStr(chars=string.ascii_uppercase, N=8):
            return ''.join(random.choice(chars) for _ in range(N))

        username = randStr(N=10)
        print("\n Trying to create user :::", username)
        return username

    def username_lowercase(self):
        def randStr(chars=string.ascii_lowercase, N=8):
            return ''.join(random.choice(chars) for _ in range(N))

        username = randStr(N=10)
        print("\n Trying to create user :::", username)
        return username

    def username_upper_lower(self):
        def randStr(chars=string.ascii_uppercase + string.ascii_lowercase, N=8):
            return ''.join(random.choice(chars) for _ in range(N))

        username = randStr(N=10)
        print("\n Trying to create user :::", username)
        return username

    def username_characters(self):
        x = Xeger(limit=34)
        regex = ReadConfig.userName_RegEx()
        name = regex
        username = x.xeger(name)
        print("\n Trying to create user :::", username)
        return username

    def username_html(self):
        username = "<fieldset name='a'>Name: <input type='text'><br>"
        print("\n Trying to create user :::", username)
        return username

    def username_javascript(self):
        username = "alert(document.getElementById('testInput').name);"
        print("\n Trying to create user :::", username)
        return username

    def username_sql(self):
        username = "select * from Admin"
        print("\n Trying to create user :::", username)
        return username

    def username_empty(self):
        username = ""
        print("\n Trying to create user :::", username)
        return username

    def username_trailing_spaces(self):
        def randStr(chars=string.ascii_uppercase, N=8):
            return ''.join(random.choice(chars) for _ in range(N))

        enterspace = "  "
        username = randStr(N=20) + enterspace
        print("\n Trying to create user :::", username)
        return username

    def username_leading_spaces(self):
        def randStr(chars=string.ascii_uppercase, N=8):
            return ''.join(random.choice(chars) for _ in range(N))

        enterspace = "  "
        username = enterspace + randStr(N=20)
        print("\n Trying to create user :::", username)
        return username

    def username_numbers(self):
        username = random.randint(1000, 9999)
        print("\n Trying to create user :::", username)
        return username

    def username_decimal(self):
        number = random.randint(0000, 9999)
        username = str(number) + "." + str(number)
        print("\n Trying to create user :::", username)
        return username

    def username_date(self):
        role = date.today()
        username = str(role)
        print("\n Trying to create user :::", username)
        
    def username_whitespace(self):
        username = "       "
        print("\n Trying to create user :", username)
        return username