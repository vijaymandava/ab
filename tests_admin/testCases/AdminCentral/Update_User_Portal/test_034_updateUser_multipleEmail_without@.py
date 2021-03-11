import pytest

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_Users import users
from tests_admin.utilities.readProperties import ReadConfig
from tests_admin.utilities.customLogger import LogGen


class Test_034_UpdateUser_MultipleEmail_AtTheRate:
    baseURL = ReadConfig.get_CM_UI_Users()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.updateuser
    def test_UpdateUser_multipleEmail_without_atTheRate_034(self,setup):
        self.logger.info("****************  Test_034:: Test UpdateUser when user sends multiple 'EmailAddress' without @ ****************")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164254?projectId=50")
        print(
            "****************  Test_034:: Test UpdateUser when user sends multiple 'EmailAddress' without @ ****************")
        print(
            "Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164254?projectId=50")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()

        self.user = users(self.driver)
        self.user.select_users_Link()

        self.user.select_edit_button()

        self.user.send_telephonenumber_textbox()
        self.driver.find_element_by_id("emailAddress").send_keys("abc.com;abc@abc.com")
        self.user.select_save_button()
        self.user.verify_error()
        try:
            self.user.firstName_RegEx()
        except Exception:
            self.user.capture_screenshot()
            self.user.select_edit_button()
        self.driver.quit()