import os
import configparser
from tests_admin.utilities.customLogger import LogGen

# Vijay
config=configparser.RawConfigParser()
config.read("./tests_admin/Configurations/config.ini")

# Chris
# file_path = os.getcwd() + r'\Configurations\config.ini'
# config = configparser.RawConfigParser()
# y = config.read(file_path)
# assert len(y)>0, ("cannot find {} are you running from the tests_admin folder?".format(file_path))

class ReadConfig():
    @staticmethod
    def get_AWS_applicationURL():
        awsurl=config.get('AWS common info','AWS_baseURL')
        return awsurl

    @staticmethod
    def get_AWS_AccountID():
        awsAccountID=config.get('AWS common info','AWS_AccountID')
        return awsAccountID

    @staticmethod
    def get_AWS_IAMUsername():
        IAM_username = config.get('AWS common info', 'AWS_IAM_username')
        return IAM_username

    @staticmethod
    def get_AWS_password():
        AWSpassword = config.get('AWS common info', 'AWS_password')
        return AWSpassword
    @staticmethod
    def get_aws_vijay_sm():
        vijay_sm = config.get('AWS common info','vijay_sm')
        return vijay_sm

    @staticmethod
    def get_aws_vijay_win10_sm():
        vijay_sm = config.get('AWS common info', 'vijay_win10_sm')
        return vijay_sm

    @staticmethod
    def get_aws_vijay_cm():
        vijay_cm = config.get('AWS common info', 'vijay_cm')
        return vijay_cm

    @staticmethod
    def get_CM_UI_Users():
        CM_UI_Users = config.get('CM UI info', 'CM_UI_Users_URL')
        return CM_UI_Users

    @staticmethod
    def get_CM_UI_Roles():
        CM_UI_Roles = config.get('CM UI info', 'CM_UI_Roles_URL')
        return CM_UI_Roles



    @staticmethod
    def vijay_sm():
        url = config.get('SM URL', 'vijay_SM')
        return url

    @staticmethod
    def pankaj_sm():
        url = config.get('SM URL', 'pankaj_SM')
        return url

    @staticmethod
    def sm():
        url = config.get('SM URL', 'SM')
        return url

    @staticmethod
    def username():
        username = config.get('Admin central login', 'username')
        return username

    @staticmethod
    def password():
        password = config.get('Admin central login', 'password')
        return password

    @staticmethod
    def system():
        system = config.get('Systems', 'vijay')
        return system

    # @staticmethod
    # def sm():
    #     url = config.get('SM URL', 'SM')
    #     # print('sm url={}'.format(url))
    #     return url

    @staticmethod
    def sm_user_interface():
        url = config.get('SM user interface', 'SM_UI')
        print('sm ui url={}'.format(url))
        return url

    @staticmethod
    def cm_for_decryption():
        cm = config.get('CM UI info', 'CM_for_decryption')
        return cm

    @staticmethod
    def cm_for_encryption():
        cm = config.get('CM UI info', 'CM_for_encryption')
        return cm

    @staticmethod
    def sm_for_encryption():
        url = config.get('SM URL', 'SM_for_encryption')
        return url

    @staticmethod
    def timeout_sm():
        timeout = int(config.get('SM user interface', 'SM_TIMEOUT'))
        return timeout

    @staticmethod
    def editedBy_RegEx():
        editedBy_Regex = config.get('Field validations', 'editedBy')
        return editedBy_Regex

    @staticmethod
    def deletedBy_RegEx():
        deletedBy_Regex = config.get('Field validations', 'deletedBy')
        return deletedBy_Regex

    @staticmethod
    def userName_RegEx():
        userName_Regex = config.get('Field validations', 'userName')
        return userName_Regex

    @staticmethod
    def firstName_RegEx():
        firstName_Regex = config.get('Field validations', 'firstName')
        return firstName_Regex

    @staticmethod
    def lastName_RegEx():
        lastName_Regex = config.get('Field validations', 'lastName')
        return lastName_Regex

    @staticmethod
    def middleInitial_RegEx():
        middleInitial_Regex = config.get('Field validations', 'middleInitial')
        return middleInitial_Regex

    @staticmethod
    def userRoleName_RegEx():
        userRoleName_Regex = config.get('Field validations', 'userRoleName')
        return userRoleName_Regex

    @staticmethod
    def password_RegEx():
        password_Regex = config.get('Field validations', 'password')
        return password_Regex

    @staticmethod
    def phoneNumber_RegEx():
        phoneNumber_Regex = config.get('Field validations', 'phoneNumber')
        return phoneNumber_Regex

    @staticmethod
    def emailAddress_RegEx():
        emailAddress_Regex = config.get('Field validations', 'emailAddress')
        return emailAddress_Regex
