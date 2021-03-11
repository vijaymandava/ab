from xeger import Xeger

from tests_admin.utilities.readProperties import ReadConfig


class middleInitial_field_validations():

    # MiddleInitial
    def middleInitial_regex(self):
        x = Xeger(limit=34)
        regex = ReadConfig.middleInitial_RegEx()
        name = regex
        middleInitial = x.xeger(name)
        print("\n Sending middle initial as :::", middleInitial)
        return middleInitial