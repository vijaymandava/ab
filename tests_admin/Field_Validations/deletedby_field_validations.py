from xeger import Xeger

from tests_admin.utilities.readProperties import ReadConfig


class deletedby_field_validations():

    # DeletedBy
    def deletedby_regex(self):
        x = Xeger(limit=34)
        regex = ReadConfig.deletedBy_RegEx()
        name = regex
        deletedBy = x.xeger(name)
        print("\n Sending deletedBy :::", deletedBy)
        return deletedBy