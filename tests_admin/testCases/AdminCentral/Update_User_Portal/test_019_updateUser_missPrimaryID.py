import pytest

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_Users import users
from tests_admin.utilities.readProperties import ReadConfig
from tests_admin.utilities.customLogger import LogGen


class Test_019_UpdateUser_missPrimaryID:
    baseURL = ReadConfig.get_CM_UI_Users()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.updateuser
    def test_UpdateUser_missPrimaryID_019(self,setup):
        self.logger.info("****************  Test_019 ::Test UpdateUser when user sends  - Miss any of the Primary ID's and send the Request(FirstName, LastName, Email ID, Telephone, password, confirmPassword) ****************")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164254?projectId=50")
        print(
            "****************  Test_019 ::Test UpdateUser when user sends  - Miss any of the Primary ID's and send the Request(FirstName, LastName, Email ID, Telephone, password, confirmPassword) ****************")
        print(
            "Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164254?projectId=50")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()

        self.user = users(self.driver)
        self.user.select_users_Link()

        self.user.select_edit_button()
        self.user.send_firstName_empty()
        self.user.send_lastName_empty()
        self.user.send_emailID_empty()
        self.user.select_system_dropdown()
        self.user.select_Role_from_dropdown()
        self.user.select_save_button()
        self.user.verify_error()

        try:
            self.user.select_save_button()
        except Exception:
            self.user.capture_screenshot()
            self.user.select_edit_button()
        self.driver.quit()