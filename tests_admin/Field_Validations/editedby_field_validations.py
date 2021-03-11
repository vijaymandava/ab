from xeger import Xeger

from tests_admin.utilities.readProperties import ReadConfig


class editedby_field_validations():

    # EditedBy
    def editedby_regex(self):
        x = Xeger(limit=34)
        regex = ReadConfig.editedBy_RegEx()
        name = regex
        editedBy = x.xeger(name)
        print("\n Sending editedBy value as:::", editedBy)
        return editedBy
