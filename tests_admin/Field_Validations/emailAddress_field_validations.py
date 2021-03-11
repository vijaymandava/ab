from xeger import Xeger

from tests_admin.utilities.readProperties import ReadConfig


class emailAddress_field_validations():

    # EmailAddress
    def email_regex(self):
        x = Xeger(limit=34)
        regex = ReadConfig.emailAddress_RegEx()
        email = regex
        emailAddress = x.xeger(email)
        print("\n Sending email :::", emailAddress)
        return emailAddress