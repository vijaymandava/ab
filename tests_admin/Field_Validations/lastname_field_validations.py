from xeger import Xeger

from tests_admin.utilities.readProperties import ReadConfig


class lastname_field_validations():

    # LastName
    def lastname_regex(self):
        x = Xeger(limit=34)
        regex = ReadConfig.lastName_RegEx()
        name = regex
        lastname = x.xeger(name)
        print("\n Sending lastname as :::", lastname)
        return lastname