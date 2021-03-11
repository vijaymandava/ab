import pytest

from tests_admin.pageObjects.Admin_central_Login import admin_central_login
from tests_admin.pageObjects.Admin_central_Users import users
from tests_admin.utilities.readProperties import ReadConfig
from tests_admin.utilities.customLogger import LogGen


class Test_038_UpdateUser_Email_64Characters:
    baseURL = ReadConfig.get_CM_UI_Users()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test_portal
    @pytest.mark.updateuser
    def test_updateUser_email_64Characters_038(self,setup):
        self.logger.info("****************  Test_038:: Test UpdateUser when user sends 'EmailAddress'  64 characters  before @ ****************")
        self.logger.info("https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164254?projectId=50")
        print(
            "****************  Test_038:: Test UpdateUser when user sends 'EmailAddress'  64 characters  before @ ****************")
        print(
            "Jama link is ::https://rapidmicrobiosystems.jamacloud.com/perspective.req#/testCases/164254?projectId=50")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.login = admin_central_login(self.driver)
        self.login.admin_login()

        self.user = users(self.driver)
        self.user.select_users_Link()

        self.user.select_edit_button()

        self.user.send_emailaddress_textbox()
        self.driver.find_element_by_id("emailAddress").send_keys("abcdefghijklmnoabcdefghijklmnoabcdefghijklmnoabcdefghijklmnoabcd@abc.com")

        self.user.select_save_button()

        try:
            self.user.select_edit_button()
        except Exception:
            self.user.capture_screenshot()
            self.user.select_edit_button()
        self.driver.quit()
