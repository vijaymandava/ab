import time
import pytest
from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Central_Manager_UserList import cm_userlist
from tests_admin.utilities.readProperties import ReadConfig
from tests_admin.utilities.customLogger import LogGen


class Test_005_CM_editUser:
    baseURL = ReadConfig.get_CM_UI_Users()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.createuser
    def test_cm_editUser_005(self,setup):
        self.logger.info("****************  Test_005:: Test Edit User ****************")
        self.logger.info("")
        print("****************  Test_005:: Test Edit User   ****************")
        print("Jama link is ::")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()
        self.cm_user = cm_userlist(self.driver)
        self.cm_user.select_CM_users_Link()
        self.cm_user.verify_CM_users_header()
        time.sleep(2)
        self.cm_user.select_edit_user_button('7WLm')
        time.sleep(2)
        creating_user = self.cm_user.send_username_textbox()
        time.sleep(2)
        self.cm_user.get_all_roles()
        self.cm_user.select_all_role()
        time.sleep(2)
        self.cm_user.select_save_button()
        self.cm_user.search_toastify(creating_user)
        self.cm_user.verify_error()
        time.sleep(1)
        try:
            print("****************  Test_005:: PASSED SUCCESSFULLY ****************")
        except Exception:
            print("****************  Test_005:: FAILED ****************")
            self.cm_user.capture_screenshot()
            self.cm_user.verify_error()
        self.driver.quit()
