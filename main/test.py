from utilities.BaseClass import BaseClass
from selenium.webdriver.common.keys import Keys

class TestOne(BaseClass):  # Inheriting from BaseClass

    # Testcase1: Verifying greeting message
    def test_case1(self):
        contact = self.driver.find_element_by_xpath("//li[@id='menu-item-9950']")
        contact.click()
        self.driver.find_element_by_name('FirstName').send_keys("sam")
        self.driver.find_element_by_name('LastName').send_keys("sam")
        self.driver.find_element_by_name('Company').send_keys("Infogix HR")
        self.driver.find_element_by_name('Email').send_keys("123@gmail.com")
        self.driver.find_element_by_name('Phone').send_keys("+353830197925")
        self.driver.find_element_by_name('HQ_Location_Country__c').send_keys("United States")
        self.driver.find_element_by_name('Industry__c').send_keys("Media & Communication")
        self.driver.find_element_by_name('Next_Step_Comments__c').send_keys("This is a coding challenge for Test Automation position Please disregard this message")
        self.driver.find_element_by_id('LblConsent_to_Processing__c').click()
        self.driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
        self.driver.implicitly_wait(5)
        greeting = self.driver.find_element_by_xpath("//h1[contains(text(),'Thank You!')]").text

        assert greeting == "Thank You!"

    #
    def test_case2(self):
        self.driver.find_element_by_class_name("logo").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_class_name("search-site").click()

        self.driver.find_element_by_class_name("searchfor").send_keys("Building Data Trust with Strategic Data Governance")
        self.driver.find_element_by_class_name("searchfor").send_keys(Keys.RETURN)
        self.driver.implicitly_wait(5)

        self.driver.find_element_by_xpath("//a[contains(text(),'Building Data Trust with Strategic Data Governance')]").click()
        self.driver.implicitly_wait(2)
        link = self.driver.find_element_by_xpath("//a[contains(text(),'regulatory compliance')]").get_attribute("href")
        #print(link)
        assert link == "https://www.infogix.com/solutions/regulatory-compliance/"









