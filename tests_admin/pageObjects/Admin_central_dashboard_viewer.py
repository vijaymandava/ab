import time

from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from tests_admin.utilities.customLogger import LogGen


class dashboard_viewer():
    logger = LogGen.loggen()
    # Header & menus
    title_header_xpath = "//*[@class='toolbar__title']"
    lnk_Users_linktext = "Users"
    lnk_Roles_linktext = "Roles"
    lnk_Viewer_linktext = "Viewer"
    lnk_Logout_linktext = "Logout"
    # Site & Instrument No
    option_site_xpath = "(//*[text()='Site :']/following-sibling::h5)[1]"
    numberOfInstruments_xpath = "//*[normalize-space()='Number of Instruments :']//following-sibling::h5"
    # Day Option
    dropdown_dayOptionClick_xpath = "(//button[contains(@class,'dropdown-toggle')])[1]"
    dropdown_daySelect_xpath = "//div[@class='dropdown-menu show']//button"
    # Custom Search
    dropdown_customSearchClick_xpath = "(//button[contains(@class,'dropdown-toggle')])[2]"
    dropdown_customSearchSelect_xpath = "//div[@class='dropdown-menu show']//button"
    textbox_customSearch_dateFrom_xpath = "(//div[contains(@class,'datepicker')]//input)[1]"
    textbox_customSearch_dateTo_xpath = "(//div[contains(@class,'datepicker')]//input)[2]"
    textbox_customSearch_SerialNo_SampleID_LIMSID_xpath = "(//div//input)[3]"
    button_Search_xpath = "//button[@id='srch']//img"
    # Site Summary
    table_siteInstrumentName_xpath = "//th[@title='{}']/ancestor::div//div[@class='react-bs-container-body']//td[{}]//a"
    table_siteInstrumentID_xpath = "//th[@title='{}']/ancestor::div//div[@class='react-bs-container-body']//td[{}]//div"
    table_siteLoaded_xpath = "//th[@title='{}']/ancestor::div//div[@class='react-bs-container-body']//td[{}]//div"
    table_siteCompleted_xpath = "//th[@title='{}']/ancestor::div//div[@class='react-bs-container-body']//td[{}]//div"
    table_siteApproved_xpath = "//th[@title='{}']/ancestor::div//div[@class='react-bs-container-body']//td[{}//div"
    table_siteFailed_xpath = "//th[@title='{}']/ancestor::div//div[@class='react-bs-container-body']//td[{}]//div"
    table_siteActive_xpath = "//th[@title='{}']/ancestor::div//div[@class='react-bs-container-body']//td[{}]//div"
    table_siteOrdered_xpath = "//th[@title='{}']/ancestor::div//div[@class='react-bs-container-body']//td[{}]//div"
    table_siteLastTestDate_xpath = "//th[@title='{}']/ancestor::div//div[@class='react-bs-container-body']//td[{}]//div"
    link_pagination_xpath = "//a[@class='page-link']"
    # Instrument Summary
    table_instrumentInstName_xpath = "//th[@title='{}']/ancestor::div//div[@class='react-bs-container-body']//td[{}]"
    table_instrumentInstID_xpath = "//th[@title='{}']/ancestor::div//div[@class='react-bs-container-body']//td[{}]"
    table_instrumentSampleID_xpath = "//th[@title='{}']/ancestor::div//div[@class='react-bs-container-body']//td[{}]"
    table_instrumentLIMSID_xpath = "//th[@title='{}']/ancestor::div//div[@class='react-bs-container-body']//td[{}]"
    table_instrumentSerialNo_xpath = "//th[@title='{}']/ancestor::div//div[@class='react-bs-container-body']//td[{}]//a"
    table_instrumentLotID_xpath = "//th[@title='{}']/ancestor::div//div[@class='react-bs-container-body']//td[{}]"
    table_instrumentLoaded_xpath = "//th[@title='{}']/ancestor::div//div[@class='react-bs-container-body']//td[{}]//div"
    table_instrumentLoadedBy_xpath = "//th[@title='{}']/ancestor::div//div[@class='react-bs-container-body']//td[{}]"
    table_instrumentStatus_xpath = "//th[@title='{}']/ancestor::div//div[@class='react-bs-container-body']//td[{}]"
    table_instrumentCFU_xpath = "//th[@title='{}']/ancestor::div//div[@class='react-bs-container-body']//td[{}]"
    table_instrumentCompleted_xpath = "//th[@title='{}']/ancestor::div//div[@class='react-bs-container-body']//td[{}]//div"
    table_instrumentApproved_xpath = "//th[@title='{}']/ancestor::div//div[@class='react-bs-container-body']//td[{}]//div"

    def __init__(self, driver):
        self.driver = driver

    def select_viewer(self):
        viewerButton = self.driver.find_element_by_link_text(self.lnk_Viewer_linktext)
        if viewerButton.is_displayed() & viewerButton.is_enabled():
            viewerButton.click()
            print("Viewer button selected")
            self.logger.info("****************  Viewer button Selected   ****************")
            title = self.driver.find_element_by_xpath(self.title_header_xpath).text
            if "Site" in title:
                print("Site summary screen is displayed")
                self.logger.info("****************  Site summary screen is displayed   ****************")
            else:
                print("Site summary screen is not displayed")
                self.logger.info("****************  Site summary screen is not displayed   ****************")
        else:
            print("Viewer button not displayed or not selected")
            self.logger.info("****************  Viewer button not displayed or not selected   ****************")
            raise Exception("FAILED")

    def verify_dashboard_header(self):
        header = self.driver.find_element_by_xpath(self.title_header_xpath).text
        if (len(header)) > 0:
            if header == 'Growth Direct - Site Summary':
                print("Dashboard header is displayed correctly")
                self.logger.info("****************  Dashboard header is displayed correctly  ****************")
            else:
                print("Incorrect Dashboard header")
                self.logger.info("****************  Incorrect Dashboard header  ****************")
        else:
            print("Dashboard header is not displayed")
            self.logger.info("****************  Dashboard header is not displayed  ****************")
            raise Exception("FAILED")

    def verify_optionsite(self):
        option = self.driver.find_element_by_xpath(self.option_site_xpath).text
        print("value" + option)
        if (len(option)) > 0:
            if option == 'Lowell':
                print("Dashboard: Default option site value is validated")
                self.logger.info(
                    "****************  Dashboard: Default option site value is validated  ****************")
            else:
                print("Dashboard: Incorrect default option site value")
                self.logger.info("****************  Dashboard: Incorrect default option site value  ****************")
        else:
            print("Dashboard: Default option site is not displayed")
            self.logger.info("****************  Dashboard: Default option site is not displayed  ****************")
            raise Exception("FAILED")

    def verify_numberOfInstrument(self):
        number = self.driver.find_element_by_xpath(self.numberOfInstruments_xpath).text
        if (len(number)) >= 0:
                if number.isnumeric():
                    print("Dashboard: Number of Instrument value displayed is " + number)
                    self.logger.info(
                        "****************  Dashboard: Number of Instrument value is " + number + "  ****************")
                else:
                    print("Dashboard: Incorrect Instrument value")
                    self.logger.info("****************  Dashboard: Incorrect Instrument value ****************")
        else:
            print("Dashboard: CM address is not configured in SM")
            self.logger.info("****************  Dashboard: CM address is not configured in SM  ****************")

    def click_dayOption_dropdown(self):
        self.driver.find_element_by_xpath(self.dropdown_dayOptionClick_xpath).click()

    def verify_dayOption_dropdown(self):
        dropdownlst = self.driver.find_elements_by_xpath(self.dropdown_daySelect_xpath)
        print(len(dropdownlst))
        if (len(dropdownlst)) > 0:
            for i in range(len(dropdownlst)):
                print('{}. {}'.format(i + 1, dropdownlst[i].text))
            if i + 1 == len(dropdownlst):
                print("Dashboard: Day dropdown options is validated")
                self.logger.info("****************  Dashboard: Day dropdown options is validated ***************")
            else:
                print("Dashboard: Day dropdown options is not validated")
                self.logger.info("****************  Dashboard: Day dropdown options is not validated ***************")
        else:
            print("Dashboard: Day dropdown options is not displayed")
            self.logger.info("****************  Dashboard: Day dropdown options is not displayed ***************")
            raise Exception("FAIL")

    def select_dayOption_dropdown(self, value):
        dropdownlst = self.driver.find_elements_by_xpath(self.dropdown_daySelect_xpath)
        print(len(dropdownlst))
        flag = 0
        if (len(dropdownlst)) > 0:
            for i in range(len(dropdownlst)):
                if value in dropdownlst[i].text:
                    dropdownlst[i].click()
                    flag = 1
                    print(flag)
                    break
            if flag != 0:
                print("Dashboard: " + value + " option is selected")
                self.logger.info("****************  Dashboard: " + value + " option is selected ***************")
            else:
                print("Dashboard: " + value + " is not displayed in the day option dropdown")
                self.logger.info(
                    "****************  Dashboard: " + value + " is not displayed in the day option dropdown ***************")
                raise Exception("FAILED")

    def click_customSearch_dropdown(self):
        self.driver.find_element_by_xpath(self.dropdown_customSearchClick_xpath).click()

    def verify_customSearch_dropdown(self):
        dropdownlst = self.driver.find_elements_by_xpath(self.dropdown_customSearchSelect_xpath)
        print(len(dropdownlst))
        if (len(dropdownlst)) > 0:
            for i in range(len(dropdownlst)):
                print('{}. {}'.format(i + 1, dropdownlst[i].text))
            if i + 1 == len(dropdownlst):
                print("Dashboard: Custom search options is validated")
                self.logger.info("****************  Dashboard: Custom search options is validated ***************")
            else:
                print("Dashboard: Custom search options is not validated")
                self.logger.info("****************  Dashboard: Custom search options is not validated ***************")
        else:
            print("Dashboard: Custom search dropdown options is not displayed")
            self.logger.info(
                "****************  Dashboard: Custom search dropdown options is not displayed ***************")
            raise Exception("FAIL")

    def select_customSearch_dropdown(self, value):
        dropdownlst = self.driver.find_elements_by_xpath(self.dropdown_customSearchSelect_xpath)
        print(len(dropdownlst))
        flag = 0
        if (len(dropdownlst)) > 0:
            for i in range(len(dropdownlst)):
                if value in dropdownlst[i].text:
                    dropdownlst[i].click()
                    flag = 1
                    print(flag)
                    break
            if flag != 0:
                print("Dashboard: " + value + " option is selected")
                self.logger.info("****************  Dashboard: " + value + " option is selected ***************")
                if (value == "Date Range"):
                    self.driver.find_element_by_xpath(self.textbox_customSearch_dateFrom_xpath).send_keys(Keys.CONTROL,
                                                                                                          'a' + Keys.NULL,
                                                                                                          '12/31/2011')
                    time.sleep(2)
                    self.driver.find_element_by_xpath(self.textbox_customSearch_dateTo_xpath).send_keys(Keys.CONTROL,
                                                                                                        'a' + Keys.NULL,
                                                                                                        '12/31/2013')
                    time.sleep(2)
                    self.driver.find_element_by_xpath(self.button_Search_xpath).click()
                    print("Dashboard: " + value + " is searched successfully")
                    self.logger.info(
                        "****************  Dashboard: " + value + " is searched successfully ****************")
                else:
                    self.driver.find_element_by_xpath(
                        self.textbox_customSearch_SerialNo_SampleID_LIMSID_xpath).send_keys("test123")
                    time.sleep(2)
                    self.driver.find_element_by_xpath(self.button_Search_xpath).click()
                    print("Dashboard: " + value + " is searched successfully")
                    self.logger.info(
                        "****************  Dashboard: " + value + " is searched successfully ****************")
            else:
                print("Dashboard: " + value + " is not displayed in the custom search dropdown")
                self.logger.info(
                    "****************  Dashboard: " + value + " is not displayed in the custom search dropdown ***************")
                raise Exception("FAILED")

    def table_verifyColumn(self, columnName, columnNo):
        tableList = self.table_siteInstrumentName_xpath.format(columnName, columnNo)
        print(len(tableList))
        if (len(tableList)) > 0:
            for i in range(len(tableList)):
                print('{}. {}'.format(i + 1, tableList[i].text))
            if i + 1 == len(tableList):

                print("Dashboard Site Summary: "+columnName+" column is displayed")
                self.logger.info("****************  Dashboard Site Summary: "+columnName+" column is displayed ***************")
            else:
                print("Dashboard Site Summary: "+columnName+" column is not displayed")
                self.logger.info("****************  Dashboard Site Summary: "+columnName+" column is not displayed ***************")
        else:
            print("Dashboard: Custom search dropdown options is not displayed")
            self.logger.info(
                "****************  Dashboard: Custom search dropdown options is not displayed ***************")
            raise Exception("FAIL")


    def table_selectColumn(self, columnName, columnNo):
        tableList = self.table_siteInstrumentName_xpath.format(columnName, columnNo)
        print("value"+tableList.text())
        if columnName == "Instrument Name":
            print("colname" + columnName)
            for i in range(len(tableList)):
                print("for")
                if columnName in tableList[i].text:
                    print("success")
                    tableList[i].click()
            for element in tableList:
                print("success")
                print(element.text)
            #self.driver.find_element_by_xpath(self.table_siteInstrumentName_xpath.format(columnName, columnNo)).click()
            print("Dashboard Viewer - Site Summary " + columnName + " is displayed")
            self.logger.info(
                "****************  Dashboard Viewer - Site Summary " + columnName + " is displayed  ****************")
            # #print("inst name"+self.table_instrumentInstName_xpath.format('Inst. Name', 1))
            # instname = self.driver.find_elements_by_xpath(self.table_instrumentInstName_xpath.format('Inst. Name', 1))
            # #print("instname"+instname)
            # for element in instname:
            #     print("success")
            #     print(element.text())
