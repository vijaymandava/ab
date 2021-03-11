import time
from idlelib import browser

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests_admin.utilities.customLogger import LogGen
from tests_admin.utilities.readProperties import ReadConfig
from selenium import webdriver


class Common_Aws_Methods():
    logger = LogGen.loggen()

    # Inputs
    input_username_id = 'username'
    input_password_id = 'password'
    input_resolving_input_id = 'resolving_input'
    input_account_id = 'account'

    # Buttons
    button_next_id = 'next_button'
    button_signin_id = 'signin_button'
    button_iam_user_radio_button_id = 'iam_user_radio_button'

    # Frame
    frame_id = 'compute-react-frame'
    button_instance_state_xpath = "//span[normalize-space()='Instance state']"
    text_instance_state_xpath = "//div[contains(text(),'Instance state')]//following-sibling::div"
    dropdown_instance_states_xpath = "//ul[@class='awsui-button-dropdown-items']//li"
    dropdown_instance_state_startInstance_xpath = "//li[@aria-label='Start instance']"
    dropdown_instance_state_stopInstance_xpath = "//li[@aria-label='Stop instance']"
    popup_xpath = "//div[@class='awsui-modal-content awsui-util-container']"
    button_popup_stop_instance_xpath = "//span[normalize-space()='Stop']"

    def __init__(self, driver):
        self.driver = driver

    def aws_login(self):
        account_id = ReadConfig.get_AWS_AccountID()
        username = ReadConfig.get_AWS_IAMUsername()
        password = ReadConfig.get_AWS_password()
        self.driver.find_element_by_id(self.button_iam_user_radio_button_id).click()
        self.driver.find_element_by_id(self.input_resolving_input_id).send_keys(account_id)
        self.driver.find_element_by_id(self.button_next_id).click()
        print("Next button clicked")
        self.driver.find_element_by_id(self.input_account_id).clear()
        self.driver.find_element_by_id(self.input_account_id).send_keys(account_id)
        self.driver.find_element_by_id(self.input_username_id).send_keys(username)
        self.driver.find_element_by_id(self.input_password_id).send_keys(password)
        self.driver.find_element_by_id(self.button_signin_id).click()

    def startInstance(self):
        self.driver.implicitly_wait(3)
        frame_id = self.driver.find_element_by_id(self.frame_id)
        self.driver.switch_to.frame(frame_id)
        status = self.driver.find_element_by_xpath(self.text_instance_state_xpath).text
        print("Instance Status : " + status)
        if status in "Running":
            print("AWS Instance is already on running state")
            self.logger.info("****************  AWS Instance is already on running state  ****************")
        else:
            instanceState = self.driver.find_element_by_xpath(self.button_instance_state_xpath)
            instanceState.click()
            time.sleep(2)
            elements = self.driver.find_elements_by_xpath(self.dropdown_instance_states_xpath)
            #print("length" + str(len(elements)))
            startInstance = self.driver.find_element_by_xpath(self.dropdown_instance_state_startInstance_xpath).text
            for element in range(len(elements)):
                #print("Instance State  ::", elements[element].text)
                if elements[element].text == startInstance:
                    if elements[element].is_enabled():
                        time.sleep(2)
                        elements[element].click()
                        wait = WebDriverWait(self.driver, 10)
                        successMessage = wait.until(EC.visibility_of_element_located(
                            (By.XPATH, "//span[contains(text(),'Successfully started')]")))
                        if successMessage:
                            print("Successfully starting AWS instance")
                            self.logger.info("****************  Successfully starting AWS instance  ****************")
                            wait = WebDriverWait(self.driver, 30)
                            wait.until(EC.visibility_of_element_located(
                                (By.XPATH,"//*[contains(text(),'Instance state')]//following-sibling::div[contains(normalize-space(),'Pending')]")))
                            wait = WebDriverWait(self.driver, 60)
                            wait.until(EC.visibility_of_element_located(
                                (By.XPATH, "//*[contains(text(),'Instance state')]//following-sibling::div[contains(normalize-space(),'Running')]")))
                            self.driver.switch_to.default_content()
                            print("Instance Status : Running")
                            print("AWS instance is up and on running state")
                            self.logger.info("****************  AWS instance is up and on running state  ****************")
                    break

    def stopInstance(self):
        self.driver.implicitly_wait(10)
        frame_id = self.driver.find_element_by_id(self.frame_id)
        self.driver.switch_to.frame(frame_id)
        status = self.driver.find_element_by_xpath(self.text_instance_state_xpath).text
        print("Instance Status : " + status)
        if status in "Stopped":
            print("AWS Instance is already on Stop state")
            self.logger.info("****************  AWS Instance is already on Stop state  ****************")
        else:
            instanceState = self.driver.find_element_by_xpath(self.button_instance_state_xpath)
            instanceState.click()
            time.sleep(2)
            elements = self.driver.find_elements_by_xpath(self.dropdown_instance_states_xpath)
            print("length" + str(len(elements)))
            stopInstance = self.driver.find_element_by_xpath(self.dropdown_instance_state_stopInstance_xpath).text
            for element in range(len(elements)):
                print("Instance State  ::", elements[element].text)
                if elements[element].text == stopInstance:
                    print(elements[element].is_enabled())
                    if elements[element].is_enabled():
                        time.sleep(2)
                        elements[element].click()
                        time.sleep(3)
                        stopButton=self.driver.find_element_by_xpath(self.button_popup_stop_instance_xpath)
                        stopButton.click()
                        wait = WebDriverWait(self.driver, 10)
                        successMessage = wait.until(EC.visibility_of_element_located(
                            (By.XPATH, "//span[contains(text(),'Successfully stopped')]")))
                        if successMessage:
                            print("Successfully stopping AWS instance")
                            self.logger.info("****************  Successfully stopping AWS instance  ****************")
                            wait = WebDriverWait(self.driver, 30)
                            wait.until(EC.visibility_of_element_located(
                                (By.XPATH,
                                 "//*[contains(text(),'Instance state')]//following-sibling::div[contains(normalize-space(),'Stopping')]")))
                            wait = WebDriverWait(self.driver, 60)
                            wait.until(EC.visibility_of_element_located(
                                (By.XPATH,
                                 "//*[contains(text(),'Instance state')]//following-sibling::div[contains(normalize-space(),'Stopped')]")))
                            self.driver.switch_to.default_content()
                            print("Instance Status : Stopped")
                            print("AWS instance is down and on stop state")
                            self.logger.info(
                                    "****************  AWS instance is down and on stop state  ****************")
                    break