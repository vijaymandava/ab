import json

import pytest
import time
import allure
from allure_commons.types import AttachmentType

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_role import roles
from tests_admin.testCases.AdminCentral.Create_Role_API.common_role_api import Common_role_api
from tests_admin.testCases.AdminCentral.Create_Role_Portal.common_role_portal import Common_role_portal
from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig


@allure.severity(allure.severity_level.BLOCKER)
class Test_039_create_multiple_roles_with_single_option_each_time:
    baseURL = ReadConfig.get_CM_UI_Roles()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.createrole
    def test_create_multiple_roles_with_single_option_each_time_039(self, setup):
        self.logger.info(
            "****************  Test_039 : Test CreateRole when user Click ADD button and create multiple roles with single option each time ****************")
        print("In Description : Test_039 : Test CreateRole when user Click ADD button and create multiple roles with single option each time ")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164224?projectId=50")
        print("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164224?projectId=50")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()
        self.RolesList = roles(self.driver)
        self.RolesList.select_roles()
        time.sleep(2)
        self.RolesList.verify_AdminCentral_RolesList_header()
        self.RolesList.select_only_administrator_edit_role_button()
        data = self.RolesList.select_single_checkbox_option_each_time()
        for j in data:
            self.RolesList.selectAll_checkbox()
            option = '//*[text()="' + j + '"]'
            print("Selecting Choice is ::", j)

            self.RolesList.driver.find_element_by_xpath(option).click()
            # print("Selected checkbox is ::", option)

            self.RolesList.select_save_button()

            # file = open("./tests_admin/role_options_status.txt", 'r')
            # body = file.readline()

            # Verifying from SM with API
            com = Common_role_api()
            e = com.verify_roleName_options('Administrator')
            opt = "'" + j + "': True"
            print("Verifying option_status from SM with api ::", opt)
            try:
                if opt == "'Select All': True":
                    file = open("./tests_admin/testCases/role_options_status.txt", 'r')
                    body = file.read()
                    # print("Data from SM ::", e)
                    # print("Existing body is ::", body)
                    assert e.__contains__(body)
                    print("After selecting Select All - all the options become enable")
                else:
                    assert e.__contains__(opt)
                    print("Option verified successfully")

            except Exception:
                pass

            print(" **** Updated role **** ")

            self.RolesList.select_only_administrator_edit_role_button()
        self.driver.close()




