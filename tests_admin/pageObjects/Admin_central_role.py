import random
import json
import time

import allure
import requests
import selenium
import urllib3
from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from tests_admin.pageObjects.common import common
from tests_admin.testCases.AdminCentral.Create_Role_API.common_role_api import Common_role_api
from tests_admin.pageObjects.Admin_central_Users import users
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class roles:
    logger = LogGen.loggen()

    # links
    lnk_Roles_linktext = "Roles"

    #Buttons
    button_Add_xpath = "//*[text() ='Add']"
    button_AddRole_popup_Save_xpath = "//button[contains(text(),'Save')]"
    button_AddRole_popup_Delete_classname = "btn-danger btn btn-primary"
    button_DeleteAll_xpath = "//button[@class='btn btn-danger ml-2 searchClass']"
    button_EDIT_xpath = "//*[contains(text(),'Edit')]"
    button_Delete_xpath = "//*[text()='Delete']"
    button_deleteRole_popup_ok_xpath = "//*[text()='Ok']"
    button_closeSymbol_xpath = "//*[text()='×']"
    button_close_xpath = "//*[text()='Close']"
    button_edit_administrator_xpath = "//*[text() = 'Administrator']//following::button[1]"

    #tittle
    tittle_Admincentral_roleList_screen_xpath = "//*[text() = 'Admin Central - Role List']"
    tittle_AddRole_popup_xpath = "//*[text()='Add Role']"
    tittle_editRole_popup_xpath = "//*[text()='Edit Role']"
    tittle_deleteRole_popup_xpath = "//*[text()='Delete Role']"

    #Textbox
    textbox_userRoleName_ID = "userRoleName"

    #Checkbox
    checkbox_selectAll_ID = "selectAll"
    checkboxes_xpath = "//*[@class='form-check-label']"
    checkbox = "//label[contains(text(),'Create Method')]"

    #Dropdown
    option_none_xpath = "//option[contains(text(),'None')]"
    list_options_xpath = "//select[@name='systemIP']"
    system = ReadConfig.system()
    # dropdown_system_xpath = "//option[contains(text(),'"+system+"')]"
    dropdown_system_xpath = "option[contains(text(), 'E02215134')]"
    dropdown_not_selectable = "//*[@class = 'form-control userRoleNameDisabled' and @name='systemIP']"

    #Toast
    toastify_xpath = "//div[contains(text(),'Failed')]"
    success_failure_tostify_xpath = "//*[@class='Toastify__toast-body']"

    #Default
    administrator_xpath = " "
    fieldservice_xpath = "//*[text()='FieldService']"
    operator_xpath = "//*[text()='Operator']"

    #Errors
    error_xpath = "//div[contains(text(),'*Please enter')]"
    initial_username_error_xpath = "//*[contains(text(),'*Please enter your username.')]"
    username_error_xpath = "//*[contains(text(),'*Please enter alphabet characters only.')]"
    firstname_error_xpath = "//*[contains(text(),'*Please enter your first name.')]"
    middleinitial_error_xpath = "//*[contains(text(),'*Please enter your middle initial.')]"
    lastname_error_xpath = "//*[contains(text(),'*Please enter your last name.')]"
    email_error_xpath = "//*[contains(text(),'*Please enter valid email-ID.')]"
    telephone_error_xpath = "//*[contains(text(),'*Please enter valid mobile no.')]"
    password_error_xpath = "//*[@id='password']/following-sibling::div"
    confirmpassword_error_xpath = "//*[@id='confirmPassword']/following-sibling::div"

    #Other
    usernames_xpath = "//*[@class='userNameColumn']"
    logout_xpath = "//*[text()='Logout']"
    select_ok_xpath = "//*[text()='Ok']"
    all_add_role_cm_options_classname = "rolesDetails"
    elements_rolelist_xpath = "//div[@class='d-flex header']//input | //div[@class='d-flex header']//button"
    elements_header_menus_xpath = "//button[@class='toggle-button']|//img|//div[@class='toolbar_navigation-items']//a"
    all_links_xpath = "//*[@class='toolbar_navigation-items']//a"
    checkbox_system_Log_xpath = "//input[@id='sendSystemLogs']"
    table_header_name_xpath="//*[text()='Name']"

    #Place Holder
    name_placeholder_xpath = "//*[@placeholder='roleName']"


    def __init__(self, driver):
        self.driver = driver

    def select_roles(self):
        wait= WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Roles")))

        self.driver.find_element_by_link_text(self.lnk_Roles_linktext).click()
        print("Role button selected")
        self.logger.info("****************  Roles button Selected   ****************")
        # try:
        #     time.sleep(2)
        #     wait = WebDriverWait(self.driver, 10)
        #     element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Edit')]")))
        #     self.driver.find_element_by_xpath(self.button_EDIT_xpath)
        #     print("Users and roles are displayed")
        #     self.logger.info("****************  Roles are displayed   ****************")
        # except Exception:
        #     print("Users and roles are not displayed")
        #     self.capture_screenshot()
        #     a = "abc"
        #     assert a == "b"

    def verify_AdminCentral_RolesList_header(self):
        header = self.driver.find_element_by_xpath(self.tittle_Admincentral_roleList_screen_xpath).text
        assert header == 'Admin Central - Role List'
        print("adminCentral_RolesList_header validated")
        self.logger.info("****************  adminCentral_RolesList_header validated  ****************")

    def select_add_role_button(self):
        # try:
        #     wait = WebDriverWait(self.driver, 10)
        #     element = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'Edit')]" )))
        #     self.driver.find_element_by_xpath(self.button_EDIT_xpath)
        # except Exception:
        #     print("Users and roles are not displayed")
        #     print("Please verify SM machine is in ON state and connected")
        #     self.logger.info("****************  Roles are not displayed   ****************")
        #     allure.attach(self.driver.get_screenshot_as_png(), name="",
        #                   attachment_type=AttachmentType.PNG)
        #     self.capture_screenshot()
        #     self.driver.quit()
        #     status = 'fail'
        #     assert status == 'Failed'
        self.driver.find_element_by_xpath(self.button_Add_xpath).click()
        addrole_header = self.driver.find_element_by_xpath(self.tittle_AddRole_popup_xpath).text
        assert addrole_header == "Add Role"
        print("add role button clicked")
        self.logger.info("****************  add role button clicked  ****************")

    def name_placeholder(self):
        placeholder = self.driver.find_element_by_xpath(self.name_placeholder_xpath).text
        assert placeholder == "roleName"

    def add_role_header(self):
        addrole_header = self.driver.find_element_by_xpath(self.tittle_AddRole_popup_xpath).text
        assert addrole_header == "Add Role"

    def verify_all_the_text_in_addrole_popup(self):
        entire_text = self.driver.find_element_by_class_name("modal-content").text
        # print("Text from addrole popup is ::", entire_text)
        # my_file = open("./tests_admin/testCases/addRolePopupScreenText.txt", "w")
        # my_file.write(entire_text)
        # my_file = open("./tests_admin/testCases/addRolePopupScreenText.txt")
        # content = my_file.read()
        file = open("./tests_admin/testCases/addRolePopupScreenText.txt", 'r')
        body = file.readline()
        # print("Data from text file ::", body
        assert entire_text.__contains__(body)
        print("All the Text in 'add_role screen' is displayed as expected")

    def verify_all_the_text_in_editrole_popup(self):
        entire_text = self.driver.find_element_by_class_name("modal-content").text
        # print("Text from addrole popup is ::", entire_text)
        # my_file = open("./tests_admin/testCases/EditRolePopupScreenText.txt", "w")
        # my_file.write(entire_text)
        # my_file = open("./tests_admin/testCases/addRolePopupScreenText.txt")
        # content = my_file.read()
        file = open("./tests_admin/testCases/EditRolePopupScreenText.txt", 'r')
        body = file.readline()
        # print("Data from text file ::", body
        assert entire_text.__contains__(body)
        print("All the Text in 'Edit_role screen' is displayed as expected")

    def total_checkboxes(self):
        checkboxes = self.driver.find_elements_by_xpath(self.checkboxes_xpath)
        list = []
        for i in checkboxes:
            data = i.text
            list.append(data)
        print("Checkboxes are :::", list)

    def verify_default_status_of_checkboxes(self):
        checkboxes = self.driver.find_elements_by_xpath(self.checkboxes_xpath)
        for i in checkboxes:
            data = i.text
            if i.is_selected():
                print(data, "  ::::  checkbox is selected/checked ")
            else:
                print(data, "::: check box is not selected/checked")

    def verify_checkbox_status(self, checkbox):
        option = '//label[contains(text(),"'+checkbox+'")]'
        print("Option is::", option)
        status = self.driver.find_element_by_xpath(option)
        if not status.is_selected():
            print("checkbox is not selected/checked ")
        else:
            print("check box is selected/checked")

    def total_checkboxes_size(self):
        checkboxes = self.driver.find_elements_by_xpath(self.checkboxes_xpath)
        list = []
        for i in checkboxes:
            data = i.text
            list.append(data)
        print("Checkboxes are :::", len(list))
        return len(list)

    def select_single_checkbox_option_each_time(self):
        checkboxes = self.driver.find_elements_by_xpath(self.checkboxes_xpath)
        list = []
        for i in checkboxes:
            data = i.text
            list.append(data)
        # print("All the options are ::", list)
        return list
            # list.append(data)
        # print("Checkboxes are :::", list)

    def send_Random_RoleName(self):
        from xeger import Xeger
        x = Xeger(limit=34)
        y = x.xeger("^[a-zA-Z]*$")
        if y == "":
            z = x.xeger("^[a-zA-Z]*$")
            time.sleep(1)
            self.driver.find_element_by_id(self.textbox_userRoleName_ID).send_keys(z)
            return z
        else:
            time.sleep(1)
            self.driver.find_element_by_id(self.textbox_userRoleName_ID).send_keys(y)
            print("Entered text in the 'Name' textbox is ::" + y)
            self.logger.info("****************  Role name entered   ****************")
            return y

    def send_existing_role_as_roleName(self):
        com = Common_role_api()
        headers = com.headers()
        url = ReadConfig.sm()
        cmurl = ReadConfig.cm_for_decryption()
        r = requests.get(url + "/getRoles", headers=headers)
        data = r.json()
        # print("Data from SM::\n", r.json())
        resp1 = requests.post(cmurl + '/encryptDecrypt/decrypt', headers=headers, data=json.dumps(data, indent=4))
        roles = resp1.json()
        # print("Roles are ::", roles)
        # extracting data in json format
        list = []
        for item in roles:
            userroles = item.get('userRoleName')
            list.append(userroles)
        a = random.choice(list)
        self.driver.find_element_by_id(self.textbox_userRoleName_ID).send_keys(a)
        print("Existing Role name entered")
        self.logger.info("**************** Existing Role name entered   ****************")

    def send_userrole_runtime(self, userrole):
        self.driver.find_element_by_id(self.textbox_userRoleName_ID).clear()
        self.driver.find_element_by_id(self.textbox_userRoleName_ID).send_keys(userrole)

    def select_default_roles(self):
        a = self.driver.find_element_by_xpath(self.administrator_xpath)
        b = self.driver.find_element_by_xpath(self.fieldservice_xpath)
        c = self.driver.find_element_by_xpath(self.operator_xpath)
        list = [a, b, c]
        b = random.choice(list)
        print("Selecting option ::", b)
        b.click()

    def select_system_from_dropdown(self):
        try:
            self.driver.find_element_by_xpath(self.dropdown_not_selectable).is_displayed()
            print("System selection - options not displayed")
        except Exception:
            self.driver.find_element_by_xpath(self.dropdown_system_xpath).click()
            print("System is selected from the dropdown")
            self.logger.info("****************  system to be connected - is selected  ****************")

    def system_options(self):
        try:
            option = self.driver.find_element_by_xpath(self.option_none_xpath).text
            assert option == "None"
            print("SM systems are not connected")

        except Exception:
            select_box = self.driver.find_element_by_name("systemIP")
            options = [x for x in select_box.find_elements_by_tag_name("option")]
            for element in options:
                print("systems connected is ::", element.get_attribute("value"),
                      "-- Related Option is(system number)::", element.text)

    def select_Random_roles_checkboxes(self):
        # identifying the checkboxes with type attribute in a list
        checkboxes = self.driver.find_elements_by_class_name('form-check-label')
        list = random.sample(checkboxes, 5)
        rolesToUncheck = []
        for i in list:
            data = i.text
            rolesToUncheck.append(data)
        print("Random options are ", rolesToUncheck)
        for checkbox in list:
            if not checkbox.is_selected():
                checkbox.click()
        print("Random checkboxes selected")
        self.logger.info("****************  Random checkboxes selected  ****************")

    def selectAll_checkbox(self):
        checked = self.driver.execute_script(("return document.getElementById('createActionAlertLevel').checked"))
        if checked == False:
            self.driver.find_element_by_id(self.checkbox_selectAll_ID).click()
        print("SelectALL box -  checked")
        self.logger.info("****************  Checked Select_all checkbox  ****************")

    def uncheck_selectAll_checkbox(self):
        checked = self.driver.execute_script(("return document.getElementById('createActionAlertLevel').checked"))
        if checked == True:
            self.driver.find_element_by_id(self.checkbox_selectAll_ID).click()
            print("SelectALL box -  unchecked")

    def select_save_button(self):
        time.sleep(2)
        element = self.driver.find_element_by_xpath("//button[contains(text(),'Save')]")
        print("Save button displayed")
        element.click()
        print("Save button selected")
        self.logger.info("****************  Save button selected  ****************")

    def get_error(self):
        errortext = self.driver.find_element_by_xpath(self.error_xpath).text
        print("Error is ", errortext)
        return errortext

    def select_closeSymbol_mark(self):
        self.driver.find_element_by_xpath(self.button_closeSymbol_xpath).click()
        print("CloseSymbol button clicked ")
        self.logger.info("****************  closeSymbol button selected  ****************")

    def select_close_button(self):
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(self.button_close_xpath).click()
        element = self.driver.find_element_by_xpath(self.button_close_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        print("Close button clicked ")
        self.logger.info("****************  close button selected  ****************")

    def search_toastify_error(self):
        wait = WebDriverWait(self.driver, 3)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Error:')]")))
        message = element.text
        print("error toast alert displayed\n", "Error ::::\n", message)
        self.logger.info("****************  Error toast popup displayed  ****************")
        return message

    def search_toastify(self, creating_role):
        time.sleep(3)
        try:
            role = self.driver.find_element_by_xpath("//*[contains(text(),'" + creating_role + "')]").text
            print("Received toast Pop_up is::", role)
            if role.__contains__('Success'):
                print("Role present in the CM UI")
                print(" :::success toast alert displayed ::::")
                self.logger.info("****************  Success toast popup displayed  ****************")
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="",
                              attachment_type=AttachmentType.PNG)
                print(" :::Failure toast alert is dispalyed")
        except Exception:
            role_name_error = "//div[contains(text(),'*Please enter alphabet characters only.')]"
            error = self.driver.find_element_by_xpath(role_name_error).text
            print("Error displayed is ::", error)
            if error.__contains__('Please'):
                print(" ::::Error displayed ::::")
            allure.attach(self.driver.get_screenshot_as_png(), name="",
                          attachment_type=AttachmentType.PNG)
            self.capture_screenshot()
            self.driver.quit()
            status = 'error'
            assert status == 'failed'

    def verify_username_error(self):
        role_name_error = "//div[contains(text(),'*Please enter alphabet characters only.')]"
        error = self.driver.find_element_by_xpath(role_name_error).text
        print("Error displayed is ::", error)
        if error.__contains__('Please'):
            print(" ::::Error displayed ::::")
        self.driver.quit()

    def verify_cm_ui_positive(self, creating_role):
        role_xpath = "//*[contains(text(),'" + creating_role + "')]"
        # Verifying toast popup
        role = self.driver.find_element_by_xpath(role_xpath).text
        print("Received toast Pop_up is::", role)
        if role.__contains__('Success'):
            print(" ::::success toast alert displayed ::::")
            self.logger.info("****************  Success toast popup displayed  ****************")
        else:
            print(" Failure toast alert displayed")
            allure.attach(self.driver.get_screenshot_as_png(), name="",
                          attachment_type=AttachmentType.PNG)
            self.logger.info("****************  Failure/Error toast popup displayed  ****************")
            # print("Creating role is::::", creating_role)
            self.driver.close()
        time.sleep(10)
        # print("role_xpath is ::", role_xpath)
        # Verify role in CM UI
        role = self.driver.find_element_by_xpath(role_xpath).text
        print("Created role is ::", role)
        assert role.__contains__(creating_role)
        print("Role present in the CM UI")

    def verify_cm_ui_negative(self, creating_role):
        role_xpath = "//*[contains(text(),'" + creating_role + "')]"
        role = self.driver.find_element_by_xpath(role_xpath).text
        print("Received toast Pop_up is::", role)
        if role.__contains__('Success'):
            print(" ::::success toast alert displayed ::::")
            self.logger.info("****************  Success toast popup displayed  ****************")
        else:
            print(" Failure toast alert displayed")
            self.logger.info("****************  Failure/Error toast popup displayed  ****************")
        # print("Creating role is::::", creating_role)
        time.sleep(5)
        # print("role_xpath is ::", role_xpath)
        role = self.driver.find_element_by_xpath(role_xpath).text
        if role.__contains__(creating_role):
            print("Role not present in the CM UI")
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="",
                          attachment_type=AttachmentType.PNG)
            print("Role not present in the CM UI")

    def search_toastify_edit_success(self):
        wait = WebDriverWait(self.driver, 3)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Edited')]")))
        message = element.text
        print(" success toast alert displayed ::::", message)
        self.logger.info("****************  Success toast popup displayed  ****************")

    def select_deleteAll_button(self):
        self.driver.find_element_by_xpath(self.button_DeleteAll_xpath).click()
        print("DeleteAll button is selected")
        self.logger.info("****************  Delete_all_button selected  ****************")

    def select_edit_role_button(self):
        self.driver.find_element_by_xpath(self.button_EDIT_xpath).click()
        print("Edit button clicked")
        self.logger.info("****************  Edit role button selected  ****************")
        tittle_text = self.driver.find_element_by_xpath(self.tittle_editRole_popup_xpath).text
        assert tittle_text == "Edit Role"
        print("Edit role - tittle displayed ")
        print("Edit Role popup screen is displayed")
        self.logger.info("****************  edit role popup displayed  ****************")

    def select_only_administrator_edit_role_button(self):
        self.driver.find_element_by_xpath(self.button_edit_administrator_xpath).click()
        print("Administrator Edit button clicked")
        tittle_text = self.driver.find_element_by_xpath(self.tittle_editRole_popup_xpath).text
        assert tittle_text == "Edit Role"
        name = self.driver.find_element_by_id(self.textbox_userRoleName_ID).get_attribute('value')
        print("name ::", name)
        assert name == 'Administrator'
        return name

    def select_delete_role_button(self):
        time.sleep(2)
        delete_buttons = self.driver.find_elements_by_xpath(self.button_Delete_xpath)
        delete = random.choice(delete_buttons)
        delete.click()
        print("Delete role button selected")
        self.logger.info("****************  Delete role button selected  ****************")

    def select_ok_button_deleteRole_popup(self):
        self.driver.find_element_by_xpath(self.button_deleteRole_popup_ok_xpath).click()
        print("Delete role 'ok' button selected")
        self.logger.info("****************  Delete role 'ok' button selected  ****************")
        wait = WebDriverWait(self.driver, 3)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='Toastify__toast-body']")))
        message = element.text
        print("Toast alert displayed ::::", message)
        list = ['Failed to delete the Role Administrator Error', 'Failed to delete the Role Operator Error',
                'Failed to delete the Role FieldService Error']
        if list.__contains__(message):
            print("Default roles can't be deleted")
        else:
            print("Role Deleted successfully")
        self.logger.info("****************  Success toast popup displayed  ****************")

    def capture_screenshot(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.driver.save_screenshot('./Screenshots/screenshot-%s.png' % now)
        allure.attach(self.driver.get_screenshot_as_png(), name="",
                      attachment_type=AttachmentType.PNG)
        self.logger.info("****************  Screenshot captured  ****************")
        print("Screenshot captured")

    def addRole_popup_tittle(self):
        popupscreen_tittle = self.driver.find_element_by_xpath(self.tittle_AddRole_popup_xpath).text
        return popupscreen_tittle

    def deleteAll_roles(self):
        url = ReadConfig.sm()
        r = requests.get(url + "/getRoles")
        # extracting data in json format
        list = []
        for item in r.json():
            userroles = item.get('userRoleName')
            list.append(userroles)
        print("Before deletion Roles are :::\n", list)
        for i in list:
            print("Deleting role :::", i)
            body = {'deletedBy': 1, 'userRoleName': i}
            url = ReadConfig.sm()
            r = requests.delete(url + "/deleteRole", data=json.dumps(body, indent=4))

        url = ReadConfig.sm()
        r = requests.get(url + "/getRoles")
        # extracting data in json format
        list = []
        for item in r.json():
            userroles = item.get('userRoleName')
            list.append(userroles)
        print("After deletion Roles list :::", list)

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

    def verify_Roles_in_SM(self):
        com = Common_role_api()
        headers = com.headers()
        url = ReadConfig.sm()
        cmurl = ReadConfig.cm_for_decryption()
        r = requests.get(url + "/getRoles", headers=headers)
        data = r.json()
        # print("Data from SM::\n", r.json())

        resp1 = requests.post(cmurl + '/encryptDecrypt/decrypt', headers=headers, data=json.dumps(data, indent=4))
        roles = resp1.json()
        # print("Roles are ::", roles)
        # extracting data in json format
        list = []
        for item in roles:
            userroles = item.get('userRoleName')
            list.append(userroles)
        # print("Roles are :::\n", list)
        return list

    def verify_roles_from_sm_UI(self, a):
        logger = LogGen.loggen()

        url_sm_ui = ReadConfig.sm_user_interface()
        http = urllib3.PoolManager()

        ######### get role ###############
        logger.info('------- get role -------')

        name = "Administrator"
        fields = {
            'name': name,
        }

        r = http.request(
            method='GET',
            url=url_sm_ui + 'roles/get_role',
            fields=fields,
            retries=False,
            timeout=120.0, )

        logger.info('response is type {}'.format(type(r)))
        logger.info('headers is type  {}'.format(type(r.headers)))
        logger.info('status is type   {}'.format(type(r.status)))
        logger.info('data is type     {}'.format(type(r.data)))
        logger.info('r.headers = {}'.format(r.headers))
        logger.info('r.status  = {}'.format(r.status))
        logger.info('r.data    = {}'.format(r.data))

        assert r.status == 200, "response has bad status"
        data = json.loads(r.data.decode('utf-8'))

        logger.info('------- work with the response data --------')
        for key, value in data.items():
            logger.info("{} {}".format(key, value))
        logger.info('there are {}'.format(len(data)))

        assert data['methods_create'] == 1
        assert data['methods_edit'] == 1
        assert data['methods_delete'] == 1
        assert data['aa_create'] == 1
        assert data['aa_edit'] == 1
        assert data['aa_delete'] == 1

        logger.info('------- test done --------')

    def select_roles_with_keyboard_tab(self):
        self.driver.implicitly_wait(5)
        links = self.driver.find_elements_by_xpath(self.all_links_xpath)
        roles_link = self.driver.find_element_by_link_text(self.lnk_Roles_linktext).text
        time.sleep(2)
        header = self.driver.find_element_by_xpath(users.tittle_Admincentral_userList_screen_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(header).click().perform()
        for element in range(len(links)):
            print(links[element].text)
            actions.send_keys(Keys.TAB)
            actions.perform()
            time.sleep(2)
            if links[element].text == roles_link:
                actions.send_keys(Keys.ENTER)
                actions.perform()
                break
        print("Roles link selected with keyboard ")
        self.logger.info("****************  Roles link selected with keyboard   ****************")

    def select_add_role_button_with_keyboard_tab(self):
        search_input = self.driver.find_element_by_id("search_input")
        elements = self.driver.find_elements_by_xpath(self.elements_rolelist_xpath)
        addbtn = self.driver.find_element_by_xpath(self.button_Add_xpath).text
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
            print("Add Role button selected with keyboard ")
            self.logger.info("****************  Add Role button selected with keyboard   ****************")

    def select_total_checkboxes_with_KeyBoard_tab(self):
        checkboxes = self.driver.find_elements_by_class_name('form-check-input')
        for checkbox in checkboxes[1:]:
            checkbox.send_keys(Keys.TAB)
            if not checkbox.is_selected():
                checkbox.send_keys(Keys.SPACE)

    def verify_roles_from_sm_with_api(self,roleName):
        com = Common_role_api()
        headers = com.headers()
        url = ReadConfig.sm()
        cmurl = ReadConfig.cm_for_decryption()
        r = requests.get(url + "/getRoles", headers=headers)
        data = r.json()
        # print("Data from SM::\n", r.json())
        resp1 = requests.post(cmurl + '/encryptDecrypt/decrypt', headers=headers, data=json.dumps(data, indent=4))
        roles = resp1.json()
        # print("Roles are ::", roles)
        # extracting data in json format
        list = []
        for item in roles:
            userroles = item.get('userRoleName')
            list.append(userroles)
        # print("Roles are :::\n", list)
        if list.__contains__(roleName):
            assert list.__contains__(roleName) == True
            print("\n Created Role present in the SM(checking with API)  ::::", roleName)
            # logger.info("****************  Role present in the SM ****************")
        else:
            assert list.__contains__(roleName) != True
            print("\n Role not present in the SM(checking with API)  ::::", roleName)
            # logger.info("****************  Role not present in the SM ****************")

    def verify_roleName_options(self, roleName):
        url = ReadConfig.sm()
        cmurl = ReadConfig.cm_for_decryption()
        com = common()
        headers = com.headers()
        # print("Verifying role ::  ", roleName)
        # Generating Token
        body = {
            "userRoleName": roleName
        }
        encryption = requests.post(cmurl + '/encryptDecrypt/encrypt', headers=headers, data=json.dumps(body, indent=4))
        encrypted_body = encryption.text
        b = json.loads(encrypted_body)
        resp = requests.post(url + '/getRole', headers=headers, data=json.dumps(b, indent=4))
        resp_text = resp.text
        d = json.loads(resp_text)
        message = d["status_message"]
        msg = json.loads(message)
        decrypt = requests.post(cmurl + '/encryptDecrypt/decrypt', headers=headers, data=json.dumps(msg, indent=4))
        decrypted_text = decrypt.text
        e = json.loads(decrypted_text)
        # print("\n Decrypted text is ::\n", e)
        # return e
        # list = []
        # for key, value in e.items():
        #     print("assert ['", key,"'] == ",value)
        #
        #     list.append(value)
        return e

    def select_roles_with_keyboard_shiftTab(self):
        self.driver.implicitly_wait(5)
        header_elements = self.driver.find_elements_by_xpath(self.elements_header_menus_xpath)
        roles_link = self.driver.find_element_by_link_text(self.lnk_Roles_linktext).text
        search_input = self.driver.find_element_by_id("search_input")
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.move_to_element(search_input).click().perform()
        i = len(header_elements)-1
        while i>=0:
            if i>3:
                actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT)
            if i<=3:
                print(i)
                time.sleep(2)
                if header_elements[i].text == roles_link:
                    actions.send_keys(Keys.ENTER).perform()
                    break
                actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT)
            i -= 1
        print("Roles link selected with keyboard shiftTab ")
        self.logger.info("****************  Roles link selected with keyboard shiftTab ****************")

    def select_add_role_button_with_keyboard_shiftTab(self):
        table_header_name = self.driver.find_element_by_xpath(self.table_header_name_xpath)
        elements = self.driver.find_elements_by_xpath(self.elements_rolelist_xpath)
        addbtn = self.driver.find_element_by_xpath(self.button_Add_xpath).text
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
            print("Add Role button selected with keyboard shiftTab")
            self.logger.info("****************  Add Role button selected with keyboard shiftTab  ****************")

    def select_total_checkboxes_with_KeyBoard_shiftTab(self):
        checkboxes = self.driver.find_elements_by_class_name('form-check-input')
        systemLog = self.driver.find_element_by_xpath(self.checkbox_system_Log_xpath)
        actions = ActionChains(self.driver)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", systemLog)
        actions.move_to_element(systemLog).click().perform()
        i = 1
        while i < len(checkboxes)-1:
            print("i"+str(i))
            actions.key_down(Keys.SHIFT).send_keys(Keys.TAB).perform()
            if not checkboxes[i].is_selected():
                actions.send_keys(Keys.SPACE).perform()
            i += 1
        save = self.driver.find_element_by_xpath("//button[contains(text(),'Save')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", save)
        print("New Role added successfully with keyboard shiftTab")
        self.logger.info("****************  New Role added successfully with keyboard shiftTab  ****************")

    def select_roles_after_zoom(self):
        time.sleep(2)
        roles_link = self.driver.find_element_by_link_text(self.lnk_Roles_linktext)
        self.driver.execute_script("document.body.style.zoom = '120%'");
        time.sleep(2)
        actions = ActionChains(self.driver)
        self.driver.execute_script("arguments[0].scrollIntoView();", roles_link)
        self.driver.execute_script("arguments[0].click();", roles_link)
        print("Roles link selected after applying zoom  ")
        self.logger.info("****************  Roles link Selected after applying zoom  ****************")

    def select_add_role_button_after_zoom(self):
        time.sleep(2)
        addbtn = self.driver.find_element_by_xpath(self.button_Add_xpath)
        self.driver.execute_script("document.body.style.zoom = '80%'");
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", addbtn)
        self.driver.execute_script("arguments[0].click();", addbtn)
        print("Add button selected after applying zoom  ")
        self.logger.info("****************  Add button Selected after applying zoom  ****************")

    def selectAll_checkbox_after_zoom(self):
        selectAll = self.driver.find_element_by_id(self.checkbox_selectAll_ID)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", selectAll)
        if not selectAll.is_selected():
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", selectAll)
        print("SelectAll checkbox selected ")
        self.logger.info("****************  SelectAll checkbox selected   ****************")

    def select_save_button_after_zoom(self):
        save = self.driver.find_element_by_xpath(self.button_AddRole_popup_Save_xpath)
        time.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", save)
        self.driver.execute_script("arguments[0].click();", save)
        print("Save button selected ")
        self.logger.info("****************  Save button selected   ****************")

    def select_roles_with_mouse(self):
        time.sleep(2)
        roles_link = self.driver.find_element_by_link_text(self.lnk_Roles_linktext)
        actions = ActionChains(self.driver)
        actions.move_to_element(roles_link).click_and_hold(roles_link).perform()
        time.sleep(1)
        actions.release().perform()
        print("Roles link selected with mouse ")
        self.logger.info("****************  Roles link selected with mouse  ****************")

    def select_add_role_button_with_mouse(self):
        time.sleep(2)
        addbtn = self.driver.find_element_by_xpath(self.button_Add_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(addbtn).click_and_hold(addbtn).perform()
        time.sleep(1)
        actions.release().perform()
        print("Add button selected with mouse ")
        self.logger.info("****************  Add button selected with mouse  ****************")
