import pytest
from selenium import webdriver
from page_objects.LoginPage import Login
from utilities.read_properties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUserEmail()
    password=ReadConfig.getPassword()
    
    logger=LogGen.loggen()
    
    def test_homePageTitle(self,setup):
        self.logger.info("**********test_homePageTitle***********")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
        else:
            self.logger.error("**********test_homePageTitle failed***********")
            self.driver.save_screenshot(".\\screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False
            
            
    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login= Login(self.driver)
        self.login.set_username(self.username)
        self.login.set_password(self.password)
        self.login.click_login()
        act_title=self.driver.title
        
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
            self.driver.close()
            assert False

