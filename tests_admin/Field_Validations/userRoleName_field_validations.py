import random
import string
from datetime import date
from xeger import Xeger

from tests_admin.utilities.readProperties import ReadConfig


class userRoleName_field_validations():

    # UserName
    def userRolename_regex(self):
        x = Xeger(limit=34)
        regex = ReadConfig.userRoleName_RegEx()
        name = regex
        roleName = x.xeger(name)
        print("\n Trying to create role :::", roleName)
        return roleName

    def userRolename_single_character(self):
        x = Xeger(limit=34)
        regex = ReadConfig.userRoleName_RegEx()
        role = x.xeger(regex)

        def randStr(chars=role, N=8):
            return ''.join(random.choice(chars) for _ in range(N))

        roleName = randStr(N=1)
        print("\n Trying to create Role", roleName)
        return roleName

    def userRolename_max_characters(self):
        def randStr(chars=string.ascii_uppercase + string.ascii_lowercase, N=8):
            return ''.join(random.choice(chars) for _ in range(N))

        roleName = randStr(N=50)
        print("\n Trying to create role :::", roleName)
        return roleName

    def userRolename_max_plus_one(self):
        def randStr(chars=string.ascii_uppercase + string.ascii_lowercase, N=8):
            return ''.join(random.choice(chars) for _ in range(N))

        roleName = randStr(N=51)
        print("\n Trying to Create role ::", roleName)
        return roleName

    def userRolename_spaces_inbetween(self):
        def randStr(chars=string.ascii_uppercase + ' ' + ' ', N=8):
            return ''.join(random.choice(chars) for _ in range(N))

        roleName = randStr(N=10)
        print("\n Trying to create role :::", roleName)
        return roleName

    def userRolename_uppercase(self):
        def randStr(chars=string.ascii_uppercase, N=8):
            return ''.join(random.choice(chars) for _ in range(N))

        roleName = randStr(N=10)
        print("\n Trying to create role :::", roleName)
        return roleName

    def userRolename_lowercase(self):
        def randStr(chars=string.ascii_lowercase, N=8):
            return ''.join(random.choice(chars) for _ in range(N))

        roleName = randStr(N=10)
        print("\n Trying to create role :::", roleName)
        return roleName

    def userRolename_upper_lower(self):
        def randStr(chars=string.ascii_uppercase + string.ascii_lowercase, N=8):
            return ''.join(random.choice(chars) for _ in range(N))

        roleName = randStr(N=10)
        print("\n Trying to create role :::", roleName)
        return roleName

    def userRolename_characters(self):
        x = Xeger(limit=34)
        roleName = x.xeger("^[a-zA-Z0-9]*$")
        print("\n Trying to create role :::", roleName)
        return roleName

    def userRolename_html(self):
        roleName = "<fieldset name='a'>Name: <input type='text'><br>"
        print("\n Trying to create role :::", roleName)
        return roleName

    def userRolename_javascript(self):
        roleName = "alert(document.getElementById('testInput').name);"
        print("\n Trying to create role :::", roleName)
        return roleName

    def userRolename_sql(self):
        roleName = "select * from Admin"
        print("\n Trying to create role :::", roleName)
        return roleName

    def userRolename_empty(self):
        roleName = ""
        print("\n Trying to create role :::", roleName)
        return roleName

    def userRolename_trailing_spaces(self):
        def randStr(chars=string.ascii_uppercase, N=8):
            return ''.join(random.choice(chars) for _ in range(N))

        enterspace = "  "
        roleName = randStr(N=20) + enterspace
        print("\n Trying to create role :::", roleName)
        return roleName

    def userRolename_leading_spaces(self):
        def randStr(chars=string.ascii_uppercase, N=8):
            return ''.join(random.choice(chars) for _ in range(N))

        enterspace = "  "
        roleName = enterspace + randStr(N=20)
        print("\n Trying to create role :::", roleName)
        return roleName

    def userRolename_numbers(self):
        roleName = random.randint(1000, 9999)
        print("\n Trying to create role :::", roleName)
        return roleName

    def userRolename_decimal(self):
        number = random.randint(0000, 9999)
        roleName = str(number) + "." + str(number)
        print("\n Trying to create role :::", roleName)
        return roleName

    def userRolename_date(self):
        role = date.today()
        roleName = str(role)
        print("\n Trying to create role :::", roleName)
