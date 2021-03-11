import datetime
import json
import random
import time
from datetime import datetime

import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from xeger import Xeger

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.testCases.AdminCentral.Create_User_API.common_createUser_api import common_createUser_api
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


class users:
    logger = LogGen.loggen()
    tittle_Admincentral_userList_screen_xpath = "//*[text() = 'Admin Central - User List']"

    #Buttons
    button_add_xpath = "//*[contains(text(),'Add')]"
    button_closeSymbol_xpath = "//*[text()='×']"
    button_save_xpath = "//*[contains(text(),'Save')]"
    button_close_xpath = "//button[contains(text(),'Close')]"
    button_DeactivateAll_xpath = "//*[contains(text(),'Deactivate All')]"
    button_EDIT_xpath = "//*[contains(text(),'Edit')]"
    button_Activate_xpath = "//*[contains(text(),'Activate')]"
    button_Deactivate_xpath = "//*[contains(text(),'Deactivate')]"
    button_ok_xpath = "//button[contains(text(),'Ok')]"

    #TextBoxes
    textbox_Username_ID = "userName"
    textbox_firstname_ID = "firstName"
    textbox_MiddleInitial_ID = "middleInitial"
    textbox_lastname_ID = "lastName"
    textbox_emailAddress_ID = "emailAddress"
    textbox_telephoneNumber_ID = "telephoneNumber"
    textbox_extension_ID="extension"
    textbox_password_ID="password"
    textbox_confirmPassword_ID="confirmPassword"

    #Dropdown
    dropdown_system_xpath="//option[contains(text(),'E12345678')]"
    dropdown_userRoleName_xpath="//*[@id='userRoleName']"

    #Links
    lnk_Users_linktext = "Users"
    lnk_logout_linktext = "Logout"


    #Default users
    default_user_administrator_xpath="//*[ contains(@class, 'userNameColumn') and contains(text(),'Administrator')]"
    default_user_FieldService_xpath="//*[ contains(@class, 'userNameColumn') and contains(text(),'FieldService')]"
    default_user_Operator_xpath="//*[ contains(@class, 'userNameColumn') and contains(text(),'Operator')]"

    #Errors
    initial_username_error_xpath = "//*[contains(text(),'*Please enter your username.')]"
    username_error_xpath = "//*[contains(text(),'*Please enter alphabet characters only.')]"
    firstname_error_xpath = "//*[contains(text(),'*Please enter your first name.')]"
    middleinitial_error_xpath = "//*[contains(text(),'*Please enter your middle initial.')]"
    lastname_error_xpath = "//*[contains(text(),'*Please enter your last name.')]"
    email_error_xpath = "//*[contains(text(),'*Please enter valid email-ID.')]"
    telephone_error_xpath = "//*[contains(text(),'*Please enter valid mobile no.')]"
    password_error_xpath = "//*[@id='password']/following-sibling::div"
    confirmpassword_error_xpath = "//*[@id='confirmPassword']/following-sibling::div"
    usernames_xpath = "//*[@class='userNameColumn']"
    logout_xpath = "//*[text()='Logout']"
    # button_ok_xpath = "//button[contains(text(),'Ok')]"
    # # button_deactivate_xpath = "//*[@class='btn btn-danger' and contains(text(),'Deactivate')]"
    # # button_activate_xpath = "//*[@class='btn btn-danger' and contains(text(),'Activate')]"


    #Place Holders
    placeholder_username_xpath = "//*[@placeholder = 'UserName']"
    placeholder_firstname_xpath = "//*[@placeholder = 'FirstName']"
    placeholder_middleInitial_xpath = "//*[@placeholder = 'Middle Initial']"
    placeholder_lastname_xpath = "//*[@placeholder = 'Last Name']"
    placeholder_emailId_xpath = "//*[@placeholder = 'Email Id']"
    placeholder_telephone_xpath = "//*[@placeholder = 'Telephone']"
    placeholder_extension_xpath = "//*[@placeholder = 'Extension']"
    placeholder_password_xpath = "//*[@placeholder = 'Password']"
    placeholder_confirmPassword_xpath = "//*[@placeholder = 'Confirm Password']"

    #Other Xpaths
    close_x_xpath = "//*[contains(text(),'×')]"
    addUser_popup_text_classname = "modal-content"
    all_links_xpath = "//*[@class='toolbar_navigation-items']//a"
    elements_rolelist_xpath = "//div[@class='d-flex header']//input | //div[@class='d-flex header']//button"
    elements_header_menus_xpath = "//button[@class='toggle-button']|//img|//div[@class='toolbar_navigation-items']//a"
    table_header_name_xpath = "//*[text()='UserName']"

    def __init__(self, driver):
        self.driver = driver

    def select_users_Link(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_link_text(self.lnk_Users_linktext).click()
        try:
            self.driver.find_element_by_xpath(self.button_EDIT_xpath)
            print("Users and roles are displayed")
        except Exception:
            self.driver.refresh()
            self.driver.find_element_by_xpath(self.lnk_logout_linktext).click()
            self.login = admin_central_login(self.driver)
            self.login.admin_login()
            self.driver.find_element_by_link_text(self.lnk_Users_linktext).click()
            self.driver.find_element_by_xpath(self.button_EDIT_xpath)
            print("Users and roles are not displayed")

    def select_add_button(self):
        try:
            time.sleep(10)
            self.driver.implicitly_wait(10)
            self.driver.find_element_by_xpath(self.button_add_xpath).click()
            time.sleep(10)
        except Exception:
            pass

    def send_username_textbox(self):
        userName = self.driver.find_element_by_id(self.textbox_Username_ID).text
        if(len(userName) == 0):
            print("UserName field is empty")
            x = Xeger(limit=34)
            y = x.xeger("^[a-zA-Z0-9]+$")
            self.driver.find_element_by_id(self.textbox_Username_ID).clear()
            self.driver.find_element_by_id(self.textbox_Username_ID).send_keys(y)
            print("Entering 'UserName'  ::" + y)
            self.logger.info("****************  UserName entered   ****************")
            return y
        else:
            userid_null = self.driver.find_element_by_id(self.textbox_Username_ID).text
            print("Username field value is :::", userName)
            self.driver.find_element_by_id(self.textbox_Username_ID).clear()
            x = Xeger(limit=34)
            y = x.xeger("^[a-zA-Z0-9]+$")
            self.driver.find_element_by_id(self.textbox_Username_ID).send_keys(y)
            print("Updated 'UserName' is ::" + y)
            self.logger.info("****************  UserName entered   ****************")
            return y

    def send_existing_username_textbox(self):
        url = ReadConfig.sm()
        headers = {'Content-Type': 'application/json'}
        a = {"userName": "CMUIServer", "password": "a5a78cfc0e4711ebadc10242ac120002"}
        resp = requests.post(url + '/getSMToken', headers=headers, data=json.dumps(a, indent=4))
        token = resp.text
        d = json.loads(token)
        message = d["status_message"]
        e = json.loads(message)
        accesstoken = "Bearer " + e["accessToken"]
        headerss = {'Content-Type': 'application/json', 'Authorization': accesstoken}
        r = requests.get(url + "/getUsers", headers=headerss)
        # print("Data from SM::\n", r.json())
        # extracting data in json format
        list = []
        for item in r.json():
            usernames = item.get('userName')
            list.append(usernames)
        print("Users are :::\n", list)
        a = random.choice(list)
        print("Sending User Name ::", a)
        self.driver.find_element_by_id(self.textbox_Username_ID).send_keys(a)

    def send_firstname_textbox(self):
        firstName = self.driver.find_element_by_id(self.textbox_firstname_ID)
        firstname_value = firstName.get_attribute("value")
        if (len(firstname_value) == 0):
            print("\n First Name field is empty")
            x = Xeger(limit=50)
            y = x.xeger("^([a-zA-Z '-]+)$")
            self.driver.find_element_by_id(self.textbox_firstname_ID).clear()
            self.driver.find_element_by_id(self.textbox_firstname_ID).send_keys(y)
            print("Entered text in the 'FirstName' textbox is ::" + y)
            self.logger.info("****************  FirstName entered   ****************")
            return y
        else:
            firstName = self.driver.find_element_by_id(self.textbox_firstname_ID)
            firstname_value = firstName.get_attribute("value")
            print("\n Existing Firstname is :::", firstname_value)
            x = Xeger(limit=50)
            y = x.xeger("^([a-zA-Z '-]+)$")
            self.driver.find_element_by_id(self.textbox_Username_ID).clear()
            self.driver.find_element_by_id(self.textbox_firstname_ID).send_keys(y)
            print("Entered text in the 'FirstName' textbox is ::" + y)
            self.logger.info("****************  FirstName entered   ****************")
            return y

    def send_middleinitial_textbox(self):
        middleinitial = self.driver.find_element_by_id(self.textbox_MiddleInitial_ID)
        middleinitial_value = middleinitial.get_attribute("value")
        if (len(middleinitial_value) == 0):
            print("\n MiddleInitial field is empty")
            x = Xeger(limit=1)
            y = x.xeger("^([a-zA-Z]+)$")
            self.driver.find_element_by_id(self.textbox_MiddleInitial_ID).clear()
            self.driver.find_element_by_id(self.textbox_MiddleInitial_ID).send_keys(y)
            print(" Entered text in the 'middleinitial' textbox is ::" + y)
            self.logger.info("****************  middleinitial entered   ****************")
            return y
        else:
            middleinitial = self.driver.find_element_by_id(self.textbox_MiddleInitial_ID)
            middleinitial_value = middleinitial.get_attribute("value")
            print("\n Existing middleInitial is :::", middleinitial_value)
            x = Xeger(limit=1)
            y = x.xeger("^([a-zA-Z]+)$")
            self.driver.find_element_by_id(self.textbox_MiddleInitial_ID).clear()
            self.driver.find_element_by_id(self.textbox_MiddleInitial_ID).send_keys(y)
            print("Entered text in the 'Middle Initial' textbox is ::" + y)
            self.logger.info("****************  Middle Initial entered   ****************")
            return y

    def send_lastname_textbox(self):
        lastname = self.driver.find_element_by_id(self.textbox_lastname_ID)
        lastname_value = lastname.get_attribute("value")
        if (len(lastname_value) == 0):
            print("\n lastname Name field is empty")
            x = Xeger(limit=50)
            y = x.xeger("^([a-zA-Z '-]+)$")
            self.driver.find_element_by_id(self.textbox_lastname_ID).clear()
            self.driver.find_element_by_id(self.textbox_lastname_ID).send_keys(y)
            print(" Entered text in the 'lastname' textbox is ::" + y)
            self.logger.info("****************  lastname entered   ****************")
            return y
        else:
            lastname = self.driver.find_element_by_id(self.textbox_MiddleInitial_ID)
            lastname_value = lastname.get_attribute("value")
            print("\n Existing lastname is :::", lastname_value)
            x = Xeger(limit=50)
            y = x.xeger("^([a-zA-Z '-]+)$")
            self.driver.find_element_by_id(self.textbox_lastname_ID).clear()
            self.driver.find_element_by_id(self.textbox_lastname_ID).send_keys(y)
            print("\n Entered text in the 'lastname' textbox is ::" + y)
            self.logger.info("****************  lastname entered   ****************")
            return y

    def send_emailaddress_textbox(self):
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_id(self.textbox_emailAddress_ID).clear()
        self.driver.find_element_by_id(self.textbox_emailAddress_ID).send_keys("abc@abc.com")
        # x = Xeger(limit=34)
        # y = x.xeger("^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$")
        # self.driver.find_element_by_id(self.textbox_emailAddress_ID).send_keys(y)
        # print("Entered text in the 'email' textbox is ::" + y)
        # self.logger.info("****************  email entered   ****************")
        # return y

    def send_telephonenumber_textbox(self):
        self.driver.find_element_by_id(self.textbox_telephoneNumber_ID).clear()
        self.driver.find_element_by_id(self.textbox_telephoneNumber_ID).send_keys('9030852544')

        # telephone = self.driver.find_element_by_id(self.textbox_telephoneNumber_ID)
        # telephone_value = telephone.get_attribute("value")
        # if (len(telephone_value) == 0):
        #     print("\n telephone Name field is empty")
        #     x = Xeger(limit=34)
        #     y = x.xeger("^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$")
        #     self.driver.find_element_by_id(self.textbox_telephoneNumber_ID).clear()
        #     self.driver.find_element_by_id(self.textbox_telephoneNumber_ID).send_keys(y)
        #
        #     # self.driver.find_element_by_id(self.textbox_telephoneNumber_ID).send_keys('(603) 595-6822')
        #     # print(" Entered text in the 'telephone' textbox is ::" + y)
        #     self.logger.info("****************  telephone entered   ****************")
        #     return y
        # else:
        #     telephone = self.driver.find_element_by_id(self.textbox_telephoneNumber_ID)
        #     telephone_value = telephone.get_attribute("value")
        #     print("\n Existing telephone is :::", telephone_value)
        #     x = Xeger(limit=34)
        #     y = x.xeger("^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$")
        #     self.driver.find_element_by_id(self.textbox_telephoneNumber_ID).clear()
        #     self.driver.find_element_by_id(self.textbox_telephoneNumber_ID).send_keys(y)
        #     # print(" Entered text in the 'telephone' textbox is ::" + y)
        #     self.logger.info("****************  Telephone entered   ****************")
        #     return y

    def send_extension_textbox(self):
        self.driver.find_element_by_id(self.textbox_extension_ID).clear()
        self.driver.find_element_by_id(self.textbox_extension_ID).send_keys('1234')

    def send_password_textbox(self):
        password = self.driver.find_element_by_id(self.textbox_password_ID)
        password_value = password.get_attribute("value")
        if (len(password_value) == 0):
            print("\n password Name field is empty")
            x = Xeger(limit=50)
            y = x.xeger("^(?=.*[0-9])(?=.*[A-Z]).{8,32}$")
            self.driver.find_element_by_id(self.textbox_password_ID).send_keys(y)
            print("Entered text in the 'password' textbox is ::" + y)
            self.logger.info("****************  password entered   ****************")
            return y
        else:
            password = self.driver.find_element_by_id(self.textbox_password_ID)
            password_value = password.get_attribute("value")
            print("\n Existing extension is :::", password_value)
            x = Xeger(limit=50)
            y = x.xeger("^(?=.*[0-9])(?=.*[A-Z]).{8,32}$")
            self.driver.find_element_by_id(self.textbox_password_ID).send_keys(y)
            print("Entered text in the 'password' textbox is ::" + y)
            self.logger.info("****************  password entered   ****************")
            return y

    def send_confirmPassword_textbox(self):
        confirmPassword = self.driver.find_element_by_id(self.textbox_confirmPassword_ID)
        confirmPassword_value = confirmPassword.get_attribute("value")
        if (len(confirmPassword_value) == 0):
            print("\n password Name field is empty")
            x = Xeger(limit=50)
            y = x.xeger("^(?=.*[0-9])(?=.*[A-Z]).{8,32}$")
            self.driver.find_element_by_id(self.textbox_confirmPassword_ID).send_keys(y)
            print("Entered text in the 'confirmpassword' textbox is ::" + y)
            self.logger.info("****************  confirmpassword entered   ****************")
            return y
        else:
            confirmPassword = self.driver.find_element_by_id(self.textbox_confirmPassword_ID)
            confirmPassword_value = confirmPassword.get_attribute("value")
            print("\n Existing confirm_password  is :::", confirmPassword_value)
            x = Xeger(limit=50)
            y = x.xeger("^(?=.*[0-9])(?=.*[A-Z]).{8,32}$")
            self.driver.find_element_by_id(self.textbox_confirmPassword_ID).send_keys(y)
            print("Entered text in the 'confirmpassword' textbox is ::" + y)
            self.logger.info("****************  confirmpassword entered   ****************")
            return y

    def send_same_password_and_confirmPassword(self):
        password = self.driver.find_element_by_id(self.textbox_password_ID)
        password_value = password.get_attribute("value")
        confirmPassword = self.driver.find_element_by_id(self.textbox_confirmPassword_ID)
        confirmPassword_value = confirmPassword.get_attribute("value")
        if (len(password_value) == 0):
            print("\n password Name field is empty")
            x = Xeger(limit=50)
            y = x.xeger("^(?=.*[0-9])(?=.*[A-Z]).{8,32}$")
            self.driver.find_element_by_id(self.textbox_password_ID).send_keys(y)
            print("Entered text in the 'password' textbox is ::" + y)
            self.logger.info("****************  password entered   ****************")
            self.driver.find_element_by_id(self.textbox_confirmPassword_ID).send_keys(y)
            print("Entered text in the 'confirmpassword' textbox is ::" + y)
            self.logger.info("****************  confirmpassword entered   ****************")
            return y
        else:
            password = self.driver.find_element_by_id(self.textbox_password_ID)
            password_value = password.get_attribute("value")
            print("\n Existing confirmpassword is :::", password_value)
            confirmPassword = self.driver.find_element_by_id(self.textbox_confirmPassword_ID)
            confirmPassword_value = confirmPassword.get_attribute("value")
            print("\n Existing confirm_password  is :::", confirmPassword_value)
            x = Xeger(limit=50)
            y = x.xeger("^(?=.*[0-9])(?=.*[A-Z]).{8,32}$")
            self.driver.find_element_by_id(self.textbox_password_ID).send_keys(y)
            print("Entered text in the 'password' textbox is ::" + y)
            self.logger.info("****************  password entered   ****************")
            self.driver.find_element_by_id(self.textbox_confirmPassword_ID).send_keys(y)
            print("Entered text in the 'confirmpassword' textbox is ::" + y)
            self.logger.info("****************  confirmpassword entered   ****************")
            return y

    def select_system_dropdown(self):
        self.driver.find_element_by_xpath(self.dropdown_system_xpath).click()

    def select_Role_dropdown(self):
        roleslist=Select(self.driver.find_element_by_xpath(self.dropdown_userRoleName_xpath))
        roles_list= self.driver.find_element_by_xpath(self.dropdown_userRoleName_xpath).text
        print("Roles list from dropdown ", roles_list)
        roleslist.select_by_index(1)

    def select_save_button(self):
        self.driver.find_element_by_xpath(self.button_save_xpath).click()

    def select_close_button(self):
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.button_close_xpath).click()

    def select_close_x(self):
        self.driver.find_element_by_xpath(self.close_x_xpath).click()

    def select_ok_button(self):
        self.driver.find_element_by_xpath(self.button_ok_xpath).click()

    def select_edit_button(self):
        ids = self.driver.find_elements_by_xpath(self.button_EDIT_xpath)
        abc = random.choice(ids)
        abc.click()

    def close(self):
        self.driver.find_element_by_xpath(self.button_close_xpath).click()

    def select_default_user(self):
        a = self.driver.find_element_by_xpath(self.default_user_administrator_xpath)
        b = self.driver.find_element_by_xpath(self.default_user_FieldService_xpath)
        c = self.driver.find_element_by_xpath(self.default_user_Operator_xpath)
        list = [a, b, c]
        randon_default_user = random.choice(list)
        return randon_default_user

    def select_default_role(self):
        sel = Select(self.driver.find_element_by_xpath(self.dropdown_userRoleName_xpath))
        a=sel.select_by_visible_text('Administrator')
        b=sel.select_by_visible_text('FieldService')
        c=sel.select_by_visible_text('Operator')
        list=[a, b, c]
        randon_default_role = random.choice(list)
        return randon_default_role

    def send_userName_update(self):
        self.driver.find_element_by_id(self.textbox_Username_ID).click()
        self.driver.find_element_by_id(self.textbox_Username_ID).send_keys('abc')

    def send_userName_runtime(self, username):
        self.driver.find_element_by_id(self.textbox_Username_ID).click()
        self.driver.find_element_by_id(self.textbox_Username_ID).send_keys(username)

    def send_firstName_empty(self):
        self.driver.find_element_by_id(self.textbox_firstname_ID).clear()

    def send_lastName_empty(self):
        self.driver.find_element_by_id(self.textbox_lastname_ID).clear()

    def send_middleInitial_empty(self):
        self.driver.find_element_by_id(self.textbox_MiddleInitial_ID).clear()

    def send_emailID_empty(self):
        self.driver.find_element_by_id(self.textbox_emailAddress_ID).clear()

    def send_telephone_empty(self):
        self.driver.find_element_by_id(self.textbox_telephoneNumber_ID).clear()

    def send_password_empty(self):
        self.driver.find_element_by_id(self.textbox_password_ID).clear()

    def send_confirmPassword_empty(self):
        self.driver.find_element_by_id(self.textbox_confirmPassword_ID).clear()

    def userName_RegEx(self):
        userName = "^[a-zA-Z0-9]+$"
        return userName

    def editedBy_RegEx(self):
        editedBy = "^[a-zA-Z0-9]+$"
        return editedBy

    def firstName_RegEx(self):
        firstName = "^([a-zA-Z '-]+)$"
        return firstName

    def middleInitial_RegEx(self):
        self.driver.find_element_by_id(self.textbox_MiddleInitial_ID).clear()
        middleInitial = "^([a-zA-Z]+)$"
        return middleInitial

    def lastName_RegEx(self):
        lastName = "^([a-zA-Z '-]+)$"
        return lastName

    def emailId_RegEx(self):
        first="^([a-zA-Z0-9_\-\.]+)$"
        last="^(\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|([a-zA-Z0-9.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$"
        # emailId = "^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$"
        x = Xeger(limit=64)
        before = x.xeger(first)
        y=Xeger(limit=256)
        after=y.xeger(last)
        emailId=before+"@"+after
        return emailId

    def telephone_RegEx(self):
        telephone = "^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$"
        return telephone

    def password_RegEx(self):
        password = "^(?=.*[0-9])(?=.*[A-Z]).{8,32}$"
        return password

    def confirmPassword_RegEx(self):
        confirmPassword = "^(?=.*[0-9])(?=.*[A-Z]).{8,32}$"
        return confirmPassword

    def capture_screenshot(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.driver.save_screenshot('./tests_admin/Screenshots/screenshot-%s.png' % now)
        self.logger.info("****************  Screenshot captured  ****************")
        print("Screenshot captured")

    def username_error(self):
        # a = self.driver.find_element_by_xpath(self.initial_username_error_xpath)
        # b = self.driver.find_element_by_xpath(self.username_error_xpath)
        if self.driver.find_element_by_xpath(self.initial_username_error_xpath).is_displayed():
            print("Error Displayed ::   *Please enter your username ")
        elif self.driver.find_element_by_xpath(self.username_error_xpath).is_displayed():
            print("Error Displayed  ::  *Please enter alphabet characters only. ")
        else:
            print("")

    def firstname_error(self):
        a=self.driver.find_element_by_xpath(self.firstname_error_xpath).text
        return a

    def middleInitial_error(self):
        a = self.driver.find_element_by_xpath(self.middleinitial_error_xpath).text
        return a

    def lastname_error(self):
        a = self.driver.find_element_by_xpath(self.lastname_error_xpath).text
        return a

    def emailid_error(self):
        a = self.driver.find_element_by_xpath(self.email_error_xpath).text
        return a

    def telephone_error(self):
        a = self.driver.find_element_by_xpath(self.telephone_error_xpath).text
        return a

    def password_error(self):
        a = self.driver.find_element_by_xpath(self.password_error_xpath).text
        return a

    def confirmpassword_error(self):
        a = self.driver.find_element_by_xpath(self.confirmpassword_error_xpath).text
        return a

    def verify_error(self):
        print("Verifyting errors")
        # Testing UserName error
        try:
            self.driver.implicitly_wait(1)
            a = self.driver.find_element_by_xpath(self.initial_username_error_xpath).text
            print("Error Displayed ::   a ")
        except Exception:
                pass

        try:
            b = self.driver.find_element_by_xpath(self.username_error_xpath).text
            print("UserName Error  ::   ", b)
        except Exception:
                pass

        # Testing firstName error
        try:
            c = self.driver.find_element_by_xpath(self.firstname_error_xpath).text
            print("FirstName Error  ::  ", c)
        except Exception:
            pass

        # Testing middleInitial
        try:
            d = self.driver.find_element_by_xpath(self.middleinitial_error_xpath).text
            print("MiddleInitial Error  ::  ", d)
        except Exception:
            pass

        # Testing lastName error
        try:
            e = self.driver.find_element_by_xpath(self.lastname_error_xpath).text
            print("lastname Error  ::  ", e)
        except Exception:
            pass

        # Testing email error
        try:
            f = self.driver.find_element_by_xpath(self.email_error_xpath).text
            print("Email Error  ::   ", f)
        except Exception:
            pass

        # Testing Telephone error
        try:
            g = self.driver.find_element_by_xpath(self.telephone_error_xpath).text
            print("telephone Error  ::  ", g)
        except Exception:
            pass

        # Testing Password error
        try:
            h = self.driver.find_element_by_xpath(self.password_error_xpath).text
            print("password Error  :: ", h)
        except Exception:
            pass

        # Testing confirm_password
        try:
            i = self.driver.find_element_by_xpath(self.confirmpassword_error_xpath).text
            print("confirmPassword  error  ::", i)
        except Exception:
            pass

    def select_edit_randomly(self):
        ids = self.driver.find_elements_by_xpath(self.button_EDIT_xpath)
        abc = random.choice(ids)
        abc.click()

    def select_activate_button(self):
        ids = self.driver.find_elements_by_xpath(self.button_Activate_xpath)
        abc = random.choice(ids)
        abc.click()

    def select_deactivate_button(self):
        ids = self.driver.find_elements_by_xpath(self.button_Deactivate_xpath)
        abc = random.choice(ids)
        abc.click()

    def select_deactivateAll_button(self):
        self.driver.find_element_by_xpath(self.button_DeactivateAll_xpath).click()

    def select_users_with_keyboard_tab(self):
        self.driver.implicitly_wait(5)
        links = self.driver.find_elements_by_xpath(self.all_links_xpath)
        users_link = self.driver.find_element_by_link_text(self.lnk_Users_linktext).text
        header = self.driver.find_element_by_xpath(self.tittle_Admincentral_userList_screen_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(header).click().perform()
        time.sleep(2)
        for element in range(len(links)):
            print(links[element].text)
            actions.send_keys(Keys.TAB)
            actions.perform()
            time.sleep(2)
            if links[element].text == users_link:
                actions.send_keys(Keys.ENTER)
                actions.perform()
                break
            print("Users link selected with keyboard ")
            self.logger.info("****************  Users link selected with keyboard   ****************")

    def select_add_user_button_with_keyboard_tab(self):
        search_input = self.driver.find_element_by_id("search_input")
        elements = self.driver.find_elements_by_xpath(self.elements_rolelist_xpath)
        addbtn = self.driver.find_element_by_xpath(self.button_add_xpath).text
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.move_to_element(search_input).click().perform()
        for element in range(len(elements))[1:]:
            print(elements[element].text)
            actions.send_keys(Keys.TAB)
            actions.perform()
            time.sleep(2)
            if elements[element].text == addbtn:
                actions.send_keys(Keys.ENTER)
                actions.perform()
                break
            print("Add User button selected with keyboard ")
            self.logger.info("****************  Add User button selected with keyboard   ****************")

    def select_users_with_keyboard_shiftTab(self):
        self.driver.implicitly_wait(5)
        header_elements = self.driver.find_elements_by_xpath(self.elements_header_menus_xpath)
        users_link = self.driver.find_element_by_link_text(self.lnk_Users_linktext).text
        search_input = self.driver.find_element_by_id("search_input")
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.move_to_element(search_input).click().perform()
        i = len(header_elements) - 1
        while i >= 0:
            if i > 3:
                actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT)
            if i <= 3:
                print(i)
                time.sleep(2)
                if header_elements[i].text == users_link:
                    actions.send_keys(Keys.ENTER).perform()
                    break
                actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT)
            i -= 1
        print("Users link selected with keyboard shiftTab ")
        self.logger.info("****************  Users link selected with keyboard shiftTab ****************")

    def select_add_user_button_with_keyboard_shiftTab(self):
        table_header_name = self.driver.find_element_by_xpath(self.table_header_name_xpath)
        elements = self.driver.find_elements_by_xpath(self.elements_rolelist_xpath)
        addbtn = self.driver.find_element_by_xpath(self.button_add_xpath).text
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.move_to_element(table_header_name).click().perform()
        i = 0
        while i <= len(elements):
            actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT)
            time.sleep(2)
            if elements[i].text == addbtn:
                actions.send_keys(Keys.ENTER).perform()
                break
            i += 1
            print("Add User button selected with keyboard shiftTab")
            self.logger.info("****************  Add User button selected with keyboard shiftTab  ****************")

    def username_placeholder(self):
        placeholder = self.driver.find_element_by_xpath(self.placeholder_username_xpath).text
        assert placeholder == "UserName"

    def firstname_placeholder(self):
        placeholder = self.driver.find_element_by_xpath(self.placeholder_firstname_xpath).text
        assert placeholder == "FirstName"

    def middleInitial_placeholder(self):
        placeholder = self.driver.find_element_by_xpath(self.placeholder_middleInitial_xpath).text
        assert placeholder == "Middle Initial"

    def lastname_placeholder(self):
        placeholder = self.driver.find_element_by_xpath(self.placeholder_lastname_xpath).text
        assert placeholder == "Last Name"

    def emailId_placeholder(self):
        placeholder = self.driver.find_element_by_xpath(self.placeholder_emailId_xpath).text
        assert placeholder == "Email Id"

    def telephone_placeholder(self):
        placeholder = self.driver.find_element_by_xpath(self.placeholder_telephone_xpath).text
        assert placeholder == "Telephone"

    def extension_placeholder(self):
        placeholder = self.driver.find_element_by_xpath(self.placeholder_extension_xpath).text
        assert placeholder == "Extension"

    def password_placeholder(self):
        placeholder = self.driver.find_element_by_xpath(self.placeholder_password_xpath).text
        assert placeholder == "Password"

    def confirmpassword_placeholder(self):
        placeholder = self.driver.find_element_by_xpath(self.placeholder_confirmPassword_xpath).text
        assert placeholder == "Confirm Password"

    def verify_placeholders(self):
        self.username_placeholder()
        self.firstname_placeholder()
        self.middleInitial_placeholder()
        self.lastname_placeholder()
        self.emailId_placeholder()
        self.telephone_placeholder()
        self.extension_placeholder()
        self.password_placeholder()
        self.confirmpassword_placeholder()

    def verify_addUser_popup_text(self):
        print("")
        entire_text = self.driver.find_element_by_class_name("modal-content").text
        # print("Text from addrole popup is ::", entire_text)
        # my_file = open("./tests_admin/testCases/addUserPopupScreenText.txt", "w")
        # my_file.write(entire_text)
        # my_file = open("./tests_admin/testCases/addUserPopupScreenText.txt")
        # content = my_file.read()
        file = open("./tests_admin/testCases/addUserPopupScreenText.txt", 'r')
        body = file.readline()
        # print("Data from text file ::", body)
        assert entire_text.__contains__(body)
        print("All the Text in 'add_user screen' is displayed as expected")


    def verify_editUser_popup_text(self):
        entire_text = self.driver.find_element_by_class_name("modal-content").text
        # print("Text from addrole popup is ::", entire_text)
        # my_file = open("./tests_admin/testCases/editUserPopupScreenText.txt", "w")
        # my_file.write(entire_text)
        file = open("./tests_admin/testCases/editUserPopupScreenText.txt", 'r')
        body = file.readline()
        # print("Data from text file ::", body)
        assert entire_text.__contains__(body)
        print("All the Text in 'edit_user screen' is displayed as expected")

    def select_add_button_after_zoom(self):
        time.sleep(2)
        addbtn = self.driver.find_element_by_xpath(self.button_add_xpath)
        self.driver.execute_script("document.body.style.zoom = '120%'");
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", addbtn)
        self.driver.execute_script("arguments[0].click();", addbtn)
        print("Add button selected after applying zoom  ")
        self.logger.info("****************  Add button Selected after applying zoom  ****************")

    def select_users_Link_after_zoom(self):
        time.sleep(2)
        users = self.driver.find_element_by_link_text(self.lnk_Users_linktext)
        self.driver.execute_script("document.body.style.zoom = '80%'");
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", users)
        self.driver.execute_script("arguments[0].click();", users)
        print("Users link selected after applying zoom  ")
        self.logger.info("****************  Users link Selected after applying zoom  ****************")

    def select_users_Link_with_mouse(self):
        time.sleep(5)
        users_link = self.driver.find_element_by_link_text(self.lnk_Users_linktext)
        actions = ActionChains(self.driver)
        actions.move_to_element(users_link).click_and_hold(users_link).perform()
        time.sleep(1)
        actions.release().perform()
        print("Users link selected with mouse ")
        self.logger.info("****************  Users link selected with mouse  ****************")

    def select_add_button_with_mouse(self):
        time.sleep(3)
        addbtn = self.driver.find_element_by_xpath(self.button_add_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(addbtn).click_and_hold(addbtn).perform()
        time.sleep(1)
        actions.release().perform()
        print("Add button selected with mouse ")
        self.logger.info("****************  Add button selected with mouse  ****************")