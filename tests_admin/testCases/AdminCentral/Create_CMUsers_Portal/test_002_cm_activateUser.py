import time
import pytest
from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Central_Manager_UserList import cm_userlist
from tests_admin.utilities.readProperties import ReadConfig
from tests_admin.utilities.customLogger import LogGen


class Test_002_CM_activateUser:
    baseURL = ReadConfig.get_CM_UI_Users()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.createuser
    def test_cm_activateUser_002(self,setup):
        self.logger.info("****************  Test_002:: Test CM Activate User ****************")
        self.logger.info("")
        print("****************  Test_002:: Test CM Activate User ****************")
        print("Jama link is ::")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()

        self.cm_user = cm_userlist(self.driver)
        self.cm_user.select_CM_users_Link()
        self.cm_user.verify_CM_users_header()
        self.cm_user.select_activate_user('7WLm')
        self.cm_user.search_toastify('7WLm')
        self.cm_user.check_status_on_user_activation('7WLm')



