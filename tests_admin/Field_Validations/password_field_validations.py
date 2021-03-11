from xeger import Xeger

from tests_admin.utilities.readProperties import ReadConfig


class password_field_validations():

    # Password
    def password_RegEx(self):
        x = Xeger(limit=20)
        regex = ReadConfig.password_RegEx()
        password_reg = regex
        password = x.xeger(password_reg)
        print("\n Trying to create password :::",password)
        return password

    def password_default(self):
        password = 'Abcd1234'
        return password

    def password_empty(self):
        password = ""
        return password

    def password_below8characters(self):
        password = 'Abcd'
        return password

    def password_above32characters(self):
        password = 'Abcd123456Abcd123456Abcd123456Abcd123456'
        return password

    def password_oneDigits_oneUpper(self):
        password = 'Abcd1234'
        return password

    def password_invalid(self):
        password = '!@#$%^&*()(*&%^&*('
        return password

