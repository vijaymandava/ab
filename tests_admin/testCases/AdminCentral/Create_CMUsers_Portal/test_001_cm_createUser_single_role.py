import time
import pytest
from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Central_Manager_UserList import cm_userlist
from tests_admin.utilities.readProperties import ReadConfig
from tests_admin.utilities.customLogger import LogGen


class Test_001_CM_CreateUser_SingleRole:
    baseURL = ReadConfig.get_CM_UI_Users()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.createuser
    def test_cm_createUser_SingleRole_001(self,setup):
        self.logger.info("****************  Test_001:: Test CM CreateUser when user Click ADD button and add name then save user. ****************")
        self.logger.info("")
        print("****************  Test_001:: Test CM CreateUser when user Click ADD button and add name then save user. ****************")
        print("Jama link is ::")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()

        self.cm_user = cm_userlist(self.driver)
        self.cm_user.select_CM_users_Link()
        self.cm_user.verify_CM_users_header()
        self.cm_user.select_add_button()
        self.cm_user.verify_add_CM_user_popup_header()
        creating_user=self.cm_user.send_username_textbox()
        time.sleep(2)
        self.cm_user.send_password_textbox()
        time.sleep(2)
        self.cm_user.check_activate_checkbox()
        time.sleep(1)
        self.cm_user.get_all_roles()
        self.cm_user.select_Random_roles_options()
        time.sleep(2)
        self.cm_user.select_save_button()
        self.cm_user.search_toastify(creating_user)
        self.cm_user.verify_error()
        time.sleep(1)
        try:
            self.cm_user.select_add_button()
        except Exception:
            self.cm_user.capture_screenshot()
            # self.cm_user.verify_error()
            self.cm_user.select_add_button()

        self.driver.quit()





