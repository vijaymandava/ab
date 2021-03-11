import datetime
import json
import random
import re
import time
import requests

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from xeger import Xeger
from selenium.webdriver.support.ui import Select

from tests_admin.testCases.AdminCentral.Create_User_API.common_createUser_api import common_createUser_api
from tests_admin.utilities.customLogger import LogGen
from datetime import datetime

from tests_admin.utilities.readProperties import ReadConfig


class cm_userlist():
    logger = LogGen.loggen()
    # Header
    title_header_xpath = "//*[@class='toolbar__title']"
    title_addUser_popup_xpath = "//*[text()='Add CM User']"
    title_editUser_popup_xpath = "//*[text()='Edit CM User']"
    title_activateUser_popup_xpath = "//*[text()='Activate CM User']"
    title_deactivateUser_popup_xpath = "//*[text()='DeActivate CM User']"

    # Links
    lnk_CMUsers_linktext = "CM Users"
    lnk_Logout_linktext = "Logout"

    # Buttons
    button_add_xpath = "//*[contains(text(),'Add')]"
    button_closeSymbol_xpath = "//*[text()='×']"
    button_save_xpath = "//*[contains(text(),'Save')]"
    button_close_xpath = "//button[contains(text(),'Close')]"
    button_DeactivateAll_xpath = "//*[contains(text(),'Deactivate All')]"
    button_EDIT_xpath = "//*[contains(text(),'Edit')]"
    button_Activate_xpath = "//*[contains(text(),'Activate')]"
    button_Deactivate_xpath = "//*[contains(text(),'Deactivate')]"
    button_ok_xpath = "//button[contains(text(),'Ok')]"

    # table
    table_header_Username_xpath = "//div[@id = 'column-username']//div"
    table_header_Roles_xpath = "//div[@id = 'column-roleNames']//div"
    table_header_Active_xpath = "//div[@id = 'column-active']//div"
    table_column_SortIcon_Username_xpath = "//div[@id = 'column-username']//span"
    table_column_SortIcon_Roles_xpath = "//div[@id = 'column-roleNames']//span"
    table_column_SortIcon_Active_xpath = "//div[@id = 'column-active']//span"
    table_columnValues_Username_xpath = "//div[contains(@class,'rdt_TableRow')]//div[2]//div"
    table_columnValues_Roles_xpath = "//div[contains(@class,'rdt_TableRow')]//div[3]//div"
    table_columnValues_Active_xpath = "//div[contains(@class,'rdt_TableRow')]//div[4]//span"
    table_columnValues_Edit_xpath = "//div[contains(@class,'rdt_TableRow')]//div[5]//button"
    table_columnValues_Activate_Deactivate_xpath = "//div[contains(@class,'rdt_TableRow')]//div[6]//button"
    table_cellvalue_Username_xpath = "//div[text()='{}']"
    table_cellvalue_Roles_xpath = "(//div[contains(text(),'{}')]//parent::div)[1]//parent::div//div[3]//div"
    table_cellvalue_Active_xpath = "(//div[contains(text(),'{}')]//parent::div)[1]//parent::div//div[4]//span"
    table_cellvalue_Edit_xpath = "(//div[contains(text(),'{}')]//parent::div)[1]//parent::div//button[contains(text(),'Edit')]"
    table_cellvalue_Activate_Deactivate_xpath = "(//div[contains(text(),'{}')]//parent::div)[1]//parent::div//button[contains(text(),'Activate')] " \
                                                "| (//div[contains(text(),'{}')]//parent::div)[1]//parent::div//button[contains(text(),'Deactivate')]"

    # Pagination
    select_rowsPerPageOptionsList_xpath = "//*[contains(text(),'Rows per page')]//following-sibling::div//select//option"
    select_rowsPerPage_xpath = "//*[contains(text(),'Rows per page')]//following-sibling::div//select"
    text_rowsDisplayed_xpath = "//*[contains(text(),'Rows per page')]//following-sibling::span"
    button_firstPage_xpath = "//button[@id='pagination-first-page']"
    button_previousPage_xpath = "//button[@id='pagination-previous-page']"
    button_nextPage_xpath = "//button[@id='pagination-next-page']"
    button_lastPage_xpath = "//button[@id='pagination-last-page']"

    # Add/Edit Form
    textbox_username_ID = "username"
    textbox_password_ID = "password"
    checkbox_activate_ID = "active"
    select_role_xpath = "//select[@id='role']"
    select_role_list_options_xpath = "//select[@id='role']//option"

    # Errors
    initial_username_error_xpath = "//*[contains(text(),'*Please enter your username.')]"
    username_error_xpath = "//*[contains(text(),'*Please enter alphabet characters only.')]"
    password_error_xpath = "//*[@id='password']/following-sibling::div"
    role_error_xpath = "//*[@id='role']/following-sibling::div"

    # Others
    text_Activate_DeActivate_popup_xpath = "//p"

    def __init__(self, driver):
        self.driver = driver

    def select_CM_users_Link(self):

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "CM Users")))
        self.driver.find_element_by_link_text(self.lnk_CMUsers_linktext).click()
        print("CM Users link selected")
        self.logger.info("****************  CM Users button Selected   ****************")

        title = self.driver.find_element_by_xpath(self.title_header_xpath).text
        if "Central Manager" in title:
            print("CM UserList page is displayed")
            self.logger.info("****************  CM UserList page is displayed  ****************")
        else:
            print("CM UserList page is not displayed")
            self.logger.info("****************  CM UserList page is not displayed   ****************")
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Edit')]")))
            self.driver.find_element_by_xpath(self.button_EDIT_xpath)
            print("CM Userlist displayed")
            self.logger.info("****************  CM Userlist are displayed   ****************")
        except Exception:
            print("CM Userlist is not displayed")
            self.capture_screenshot()
            raise Exception("FAILED")

    def verify_CM_users_header(self):
        header = self.driver.find_element_by_xpath(self.title_header_xpath).text
        print("CM Users Page Header :: " + header)
        if (len(header)) > 0:
            if header == 'Central Manager - User List':
                print("CM Users header is displayed correctly")
                self.logger.info("****************  CM Users header is displayed correctly  ****************")
            else:
                print("Incorrect CM Users header")
                self.logger.info("****************  Incorrect CM Users header  ****************")
        else:
            print("CM Users header is not displayed")
            self.logger.info("****************  CM Users header is not displayed  ****************")
            raise Exception("FAILED")

    def select_add_button(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Add')]")))
            self.driver.find_element_by_xpath(self.button_add_xpath).click()
            time.sleep(3)
            print("Add button clicked")
            self.logger.info("****************  Add button clicked  ****************")
        except Exception:
            raise Exception("Add button is not clicked")

    def verify_add_CM_user_popup_header(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Add CM User']")))
        add_header = self.driver.find_element_by_xpath(self.title_addUser_popup_xpath).text
        print("CM User Add popup header :: " + add_header)
        if (len(add_header)) > 0:
            if add_header == 'Add CM User':
                print("CM Users Add popup header is displayed correctly")
                self.logger.info("****************  CM Users Add popup header is displayed correctly  ****************")
            else:
                print("Incorrect CM Users Add popup header")
                self.logger.info("****************  Incorrect CM Users Add popup header  ****************")
        else:
            print("CM Users Add popup header is not displayed")
            self.logger.info("****************  CM Users Add popup header is not displayed  ****************")
            raise Exception("FAILED")

    def send_username_textbox(self):
        username = self.driver.find_element_by_id(self.textbox_username_ID).text
        if (len(username) == 0):
            print("Username field is empty")
            x = Xeger(limit=50)
            y = x.xeger("^[0-9A-Z]{1,50}$")
            self.driver.find_element_by_id(self.textbox_username_ID).clear()
            self.driver.find_element_by_id(self.textbox_username_ID).send_keys(y)
            print("Entering 'Username'  ::" + y)
            self.logger.info("****************  Username entered   ****************")
            return y
        else:
            print("Username field value is :::", username)
            self.driver.find_element_by_id(self.textbox_username_ID).clear()
            x = Xeger(limit=50)
            y = x.xeger("^[a-zA-Z0-9]+$")
            self.driver.find_element_by_id(self.textbox_username_ID).send_keys(y)
            print("Updated 'Username' is ::" + y)
            self.logger.info("****************  Username entered   ****************")
            return y

    def send_password_textbox(self):
        password = self.driver.find_element_by_id(self.textbox_password_ID)
        password_value = password.get_attribute("value")
        if (len(password_value) == 0):
            print("\n password Name field is empty")
            x = Xeger(limit=50)
            # y = x.xeger("^(?=.{8,32}$)(?=.*[A-Z])(?=.*[0-9]).*")
            # y=x.xeger("^[A-Z][0-9]*.{8,32}$")
            y = x.xeger("^[0-9A-Z]{8,32}$")
            print(y)
            # y = x.xeger("^(?=.*[0-9])(?=.*[A-Z]).{8,32}$")
            # x.xeger("^[a-zA-Z0-9]+$")
            self.driver.find_element_by_id(self.textbox_password_ID).clear()
            self.driver.find_element_by_id(self.textbox_password_ID).send_keys(y)
            print("Entered text in the 'password' textbox is ::" + y)
            self.logger.info("****************  password entered   ****************")
            return y
        else:
            print("\n Existing extension is :::", password_value)
            x = Xeger(limit=50)
            y = x.xeger("^[0-9A-Z]{8,32}$")
            self.driver.find_element_by_id(self.textbox_password_ID).clear()
            self.driver.find_element_by_id(self.textbox_password_ID).send_keys(y)
            print("Entered text in the 'password' textbox is ::" + y)
            self.logger.info("****************  password entered   ****************")
            return y

    def check_activate_checkbox(self):
        checked = self.driver.execute_script("return document.getElementById('active').checked")
        if not checked:
            self.driver.find_element_by_id(self.checkbox_activate_ID).click()
        print("Activate box - checked")
        self.logger.info("****************  Checked Activate checkbox  ****************")

    def uncheck_activate_checkbox(self):
        checked = self.driver.execute_script("return document.getElementById('active').checked")
        if checked:
            self.driver.find_element_by_id(self.checkbox_activate_ID).click()
        print("Activate box - unchecked")
        self.logger.info("****************  Unchecked Activate checkbox  ****************")

    def get_all_roles(self):
        select_roles = Select(self.driver.find_element_by_xpath(self.select_role_xpath))
        for option in select_roles.options:
            print("Role Options : " + option.text)

    def select_all_role(self):
        select_roles = Select(self.driver.find_element_by_xpath(self.select_role_xpath))
        select_roles.select_by_index(0)
        time.sleep(2)
        actions = ActionChains(self.driver)
        # for option in select_roles.options:
        # print("Role Options : "+option.text)
        # actions.move_to_element(option).click_and_hold(option).perform()
        # time.sleep(1)

        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

        print("All Roles selected ")
        self.logger.info("****************  All Roles selected   ****************")

    def select_single_role_runtime(self, value):
        Role_lst = Select(self.driver.find_element_by_xpath(self.select_role_xpath))
        print(len(Role_lst.options))
        flag = 0
        if (len(Role_lst.options)) > 0:
            for i in range(len(Role_lst.options)):
                print(Role_lst.options[i].text)
                time.sleep(1)
                actions = ActionChains(self.driver)
                self.driver.execute_script("arguments[0].scrollIntoView();", Role_lst.options[i])
                if value in Role_lst.options[i].text:
                    print(value + " option is present in the role dropdown")
                    Role_lst.options[i].click()
                    flag = 1
                    print(flag)
                    break
            if flag != 0:
                print("CM Add User: " + value + " role is selected")
                self.logger.info("****************  CM Add User: " + value + " role is selected ***************")
            else:
                print("CM Add User: " + value + " is not displayed in the role dropdown")
                self.logger.info(
                    "****************  CM Add User: " + value + " is not displayed in the role dropdown ***************")
                raise Exception("FAILED")

    def select_Random_roles_options(self):
        Role_lst = Select(self.driver.find_element_by_xpath(self.select_role_xpath))
        list = random.sample(Role_lst.options, 3)
        rolesToSelect = []
        for i in list:
            data = i.text
            rolesToSelect.append(data)
        print("Random options are ", rolesToSelect)
        for role in list:
            actions = ActionChains(self.driver)
            if not role.is_selected():
                actions.key_down(Keys.CONTROL).move_to_element(role).click_and_hold(role).release().perform()
                time.sleep(1)
        print("Random roles selected")
        self.logger.info("****************  Random roles selected  ****************")

    def select_save_button(self):
        time.sleep(2)
        save = self.driver.find_element_by_xpath(self.button_save_xpath)
        print("Save button displayed")
        save.click()
        print("Save button selected")
        self.logger.info("****************  Save button selected  ****************")

    def select_close_button(self):
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(self.button_close_xpath).click()
        close = self.driver.find_element_by_xpath(self.button_close_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(close).perform()
        print("Close button clicked ")
        self.logger.info("****************  close button selected  ****************")

    def select_edit_user_button(self, username):
        self.driver.find_element_by_xpath(self.table_cellvalue_Edit_xpath.format(username)).click()
        print("Edit button clicked")
        self.logger.info("****************  Edit button selected  ****************")
        title_text = self.driver.find_element_by_xpath(self.title_editUser_popup_xpath).text
        assert title_text == "Edit CM User"
        print("Edit CM User - title displayed ")
        print("Edit CM User popup screen is displayed")
        self.logger.info("****************  Edit CM User popup displayed  ****************")

    def select_activate_user(self, username):
        time.sleep(2)
        element = self.driver.find_element_by_xpath(
            self.table_cellvalue_Activate_Deactivate_xpath.format(username, username))
        print("value" + element.text)
        if element.text == "Activate":
            element.click()
            print("Activate button selected")
            self.logger.info("****************  Activate button selected  ****************")
            title_text = self.driver.find_element_by_xpath(self.title_activateUser_popup_xpath).text
            assert title_text == "Activate CM User"
            print("Activate CM User popup displayed")
            self.logger.info("****************  Activate CM User popup displayed  ****************")
            message = self.driver.find_element_by_xpath(self.text_Activate_DeActivate_popup_xpath)
            if username in message.text:
                self.driver.find_element_by_xpath(self.button_ok_xpath).click()
                print("Activating CM User Successfully")
                self.logger.info("****************  Activating CM User Successfully  ****************")
            else:
                self.driver.find_element_by_xpath(self.button_close_xpath).click()
                print("Closed Activate CM User Popup")
                self.logger.info("****************  Closed Activate CM User Popup  ****************")
        else:
            assert element.text == "Deactivate"
            print("CM User " + username + " is already in active state")
            self.logger.info("****************  CM User " + username + " is already in active state  ****************")

    def check_status_on_user_activation(self, username):
        time.sleep(2)
        element = self.driver.find_element_by_xpath(
            self.table_cellvalue_Activate_Deactivate_xpath.format(username, username))
        if element.text == "Deactivate":
            print(username + " user is in Activated State")
            self.logger.info("****************  " + username + " user is in Activated State  ****************")
        else:
            print(username + " user is not activated successfully")
            self.logger.info("****************  " + username + " user is not activated successfully ****************")

    def select_Deactivate_user(self, username):
        time.sleep(2)
        element = self.driver.find_element_by_xpath(
            self.table_cellvalue_Activate_Deactivate_xpath.format(username, username))
        print("value" + element.text)
        if element.text == "Deactivate":
            element.click()
            print("Deactivate button selected")
            self.logger.info("****************  Deactivate button selected  ****************")
            title_text = self.driver.find_element_by_xpath(self.title_deactivateUser_popup_xpath).text
            assert title_text == "DeActivate CM User"
            print("Deactivate CM User popup displayed")
            self.logger.info("****************  Deactivate CM User popup displayed  ****************")
            message = self.driver.find_element_by_xpath(self.text_Activate_DeActivate_popup_xpath)
            if username in message.text:
                self.driver.find_element_by_xpath(self.button_ok_xpath).click()
                print("DeActivated CM User Successfully")
                self.logger.info("****************  DeActivated CM User Successfully  ****************")
            else:
                self.driver.find_element_by_xpath(self.button_close_xpath).click()
                print("Closed Deactivate CM User Popup")
                self.logger.info("****************  Closed Deactivate CM User Popup  ****************")
        else:
            assert element == "Activate"
            print("CM User " + username + " is already in deactive state")
            self.logger.info(
                "****************  CM User " + username + " is already in deactive state  ****************")

    def check_status_on_user_deactivation(self, username):
        time.sleep(2)
        element = self.driver.find_element_by_xpath(
            self.table_cellvalue_Activate_Deactivate_xpath.format(username, username))
        if element.text == "Activate":
            print(username + " user is in Deactivated State")
            self.logger.info("****************  " + username + " user is in Deactivated State  ****************")
        else:
            print(username + " user is not deactivated successfully")
            self.logger.info("****************  " + username + " user is not deactivated successfully ****************")

    def search_toastify(self, creating_user):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='Toastify__toast-body']")))
        message = self.driver.find_element_by_xpath("//div[@class='Toastify__toast-body']")
        self.driver.execute_script("arguments[0].scrollIntoView();", message)
        # self.driver.execute_script("arguments[0].click();", roles_link)
        print("Received toast Pop_up is::", message.text)
        if "Success" in message.text and creating_user in message.text:
            print(" ::::success toast alert displayed ::::")
            self.logger.info("****************  Success toast popup displayed  ****************")
        else:
            print("Failure toast alert displayed")
            self.logger.info("****************  Failure/Error toast popup displayed  ****************")
            allure.attach(self.driver.get_screenshot_as_png(), name="",
                          attachment_type=AttachmentType.PNG)
            self.capture_screenshot()
            self.driver.quit()
            raise Exception("FAILED")
        time.sleep(5)
        print("Created user is ::", creating_user)

    def username_error(self):
        try:
            self.driver.implicitly_wait(1)
            err = self.driver.find_element_by_xpath(self.initial_username_error_xpath).text
            print("Error Displayed ::  ", err)
        except Exception:
            pass

        try:
            err = self.driver.find_element_by_xpath(self.username_error_xpath).text
            print("UserName Error  ::  " + err)
        except Exception:
            pass

    def password_error(self):
        try:
            err = self.driver.find_element_by_xpath(self.password_error_xpath).text
            print("password Error  :: " + err)
        except Exception:
            pass

    def role_error(self):
        try:
            h = self.driver.find_element_by_xpath(self.role_error_xpath).text
            print("Role Error  :: " + h)
        except Exception:
            pass

    def verify_error(self):
        print("Verifying errors")
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

        # Testing Password error
        try:
            h = self.driver.find_element_by_xpath(self.password_error_xpath).text
            print("password Error  :: ", h)
        except Exception:
            pass

        # Testing Role error
        try:
            h = self.driver.find_element_by_xpath(self.role_error_xpath).text
            print("Role Error  :: ", h)
        except Exception:
            pass

    def verify_users_from_sm_with_api(self,roleName):
        com = common_createUser_api()
        headers = com.headers()
        url = ReadConfig.sm()
        cmurl = ReadConfig.cm_for_decryption()
        r = requests.get(url + "/getCMUsersList", headers=headers)
        data = r.json()
        # print("Data from SM::\n", r.json())
        resp1 = requests.post(cmurl + '/encryptDecrypt/decrypt', headers=headers, data=json.dumps(data, indent=4))
        roles = resp1.json()
        # print("Roles are ::", roles)
        # extracting data in json format
        list = []
        for item in roles:
            userroles = item.get('username')
            list.append(userroles)
        # print("Roles are :::\n", list)
        if list.__contains__(roleName):
            assert list.__contains__(roleName) == True
            print("\n Created User present in the SM(checking with API)  ::::", roleName)
            # logger.info("****************  Role present in the SM ****************")
        else:
            assert list.__contains__(roleName) != True
            print("\n User not present in the SM(checking with API)  ::::", roleName)
            # logger.info("****************  Role not present in the SM ****************")


    def send_existing_CM_username_textbox(self):
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
        r = requests.get(url + "/getCMUsersList", headers=headerss)
        print("Data from SM::\n", r.json())
        # extracting data in json format

        list = []
        for item in r.json():
            usernames = item.get('username')
            list.append(usernames)
        print("Users are :::\n", list)
        a = random.choice(list)
        print("Sending User Name ::", a)
        self.driver.find_element_by_id(self.textbox_username_ID).send_keys(a)

    def check_default_rows_per_page(self):
        rows_lst = Select(self.driver.find_element_by_xpath(self.select_rowsPerPage_xpath))
        row_value = rows_lst.first_selected_option.text
        print("Rows per page displayed is "+row_value)
        if row_value == "5":
            print("Default Row value is validated")
        else:
            print("Default Row value is not 5")
            raise Exception("FAILED")

    def select_rows_per_page(self, value):
        self.driver.find_element_by_xpath(self.select_rowsPerPage_xpath).click()
        time.sleep(2)
        rows_lst = Select(self.driver.find_element_by_xpath(self.select_rowsPerPage_xpath))
        print(len(rows_lst.options))
        flag = 0
        if (len(rows_lst.options)) > 0:
            for i in range(len(rows_lst.options)):
                print(rows_lst.options[i].text)
                time.sleep(1)
                actions = ActionChains(self.driver)
                #self.driver.execute_script("arguments[0].scrollIntoView();", rows_lst.options[i])
                if value in rows_lst.options[i].text:
                    print(value + " option is present in the role dropdown")
                    rows_lst.options[i].click()
                    flag = 1
                    print(flag)
                    break
            if flag != 0:
                print("Rows per page: " + value + " is selected")
                self.logger.info("****************  Rows per page: " + value + " is selected ***************")
                time.sleep(2)
                row_value = rows_lst.first_selected_option.text
                time.sleep(2)
                if row_value == value:
                    print("User list is displayed as per the rows selected")
                else:
                    print("User list is not displayed as per the rows selected")
                    raise Exception("FAILED")
            else:
                print("Rows per page: " + value + " is not displayed in the dropdown")
                self.logger.info(
                    "****************  Rows per page: " + value + " is not displayed in the dropdown ***************")
                raise Exception("FAILED")

    def capture_screenshot(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.driver.save_screenshot('./Screenshots/screenshot-%s.png' % now)
        allure.attach(self.driver.get_screenshot_as_png(), name="",
                      attachment_type=AttachmentType.PNG)
        self.logger.info("****************  Screenshot captured  ****************")
        print("Screenshot captured")


