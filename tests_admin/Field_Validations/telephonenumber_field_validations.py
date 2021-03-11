from xeger import Xeger

from tests_admin.utilities.readProperties import ReadConfig


class telephonenumber_field_validations():

    def telephonenumber_regex(self):
        x = Xeger(limit=34)
        regex = ReadConfig.phoneNumber_RegEx()
        phone_reg = regex
        telephoneNumber = x.xeger(phone_reg)
        print("\n Sending telephone number as :::", telephoneNumber)
        return telephoneNumber

    def telephone_begin_with_space(self):
        x = Xeger(limit=34)
        regex = ReadConfig.phoneNumber_RegEx()
        telephone = regex
        telephoneNumber =' '+x.xeger(telephone)
        print("\n Sending telephone number which begin with space :::", telephoneNumber)
        return telephoneNumber

    def telephone_end_with_space(self):
        x = Xeger(limit=34)
        regex = ReadConfig.phoneNumber_RegEx()
        telephone = regex
        telephoneNumber = x.xeger(telephone)+' '
        print("\n Sending telephone number which end with space :::", telephoneNumber)
        return telephoneNumber

    def telephone_begin_end_with_space(self):
        x = Xeger(limit=34)
        regex = ReadConfig.phoneNumber_RegEx()
        telephone = regex
        telephoneNumber = ' ' +x.xeger(telephone) + ' '
        print("\n Sending telephone number which begin and end with space :::", telephoneNumber)
        return telephoneNumber