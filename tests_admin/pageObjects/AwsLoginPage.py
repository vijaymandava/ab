from selenium import webdriver

class AwsLogin:
    textbox_Accountid_id="account"
    textbox_IAMuserName_id="username"
    textbox_password_id="password"
    button_signin_id="signin_button"
    radiobutton_IAMuser_id="aws-signin-general-user-selection-iam"
    button_next_id="next_button"
    accountID_id="resolving_input"
    def __init__(self, driver):
        self.driver = driver

    def setAccountid(self,accountid):
        self.driver.find_element_by_id(self.textbox_Accountid_id).clear()
        self.driver.find_element_by_id(self.textbox_Accountid_id).send_keys(accountid)

    def setIAMuserName(self,IAMuserName):
        self.driver.find_element_by_id(self.textbox_IAMuserName_id).clear()
        self.driver.find_element_by_id(self.textbox_IAMuserName_id).send_keys(IAMuserName)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickSignin(self):
        self.driver.find_element_by_id(self.button_signin_id).click()

    def selectIAMuser(self):
        self.driver.find_element_by_id(self.radiobutton_IAMuser_id).click()

    def selectNextButton(self):
        self.driver.find_element_by_id(self.button_next_id).click()

    def sendAccountID(self,AccountID):
        self.driver.find_element_by_id(self.accountID_id).send_keys(AccountID)