from xeger import Xeger

from tests_admin.utilities.readProperties import ReadConfig


class firstname_field_validations():

    # FirstName
    def firstname_regex(self):
        x = Xeger(limit=34)
        regex = ReadConfig.firstName_RegEx()
        name = regex
        username = x.xeger(name)
        print("\n Sending firstname as :::", username)
        return username