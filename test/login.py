import unittest
import time
import configparser
import argparse
import os,sys,platform
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

class Login(unittest.TestCase):
    
    def setUp(self):
        self.browser = args.browser
        """function to get all variable from config file"""
        self.config = configparser.ConfigParser(interpolation=None)
        self.config.read('./data/config.ini')
        self.password = os.environ.get('PASSWORD')
        self.wrong_password = os.environ.get('WRONGPASSWORD')
        # creating a new browser session
        if platform.system() == 'Windows':
            if self.browser == 'chrome':
                chrome_path = self.config['path']['ChromePathWindow'] #path of your local chrome driver
                self.driver = webdriver.Chrome(chrome_path) #creating instance of chrome weddriver
            else:
                firefox_path = self.config['path']['FirefoxPathWindow'] #path of your local firefox driver
                self.driver = webdriver.Firefox(executable_path=firefox_path) #creating instance of firefox weddriver
        elif platform.system() == 'Linux':
            if self.browser == 'chrome':
                chrome_path = self.config['path']['ChromePathLinux'] #path of your local chrome driver
                self.driver = webdriver.Chrome(chrome_path)  #creating instance of chrome weddriver
            else:
                firefox_path = self.config['path']['FirefoxPathMAC'] #path of your local firefox driver
                self.driver = webdriver.Firefox(executable_path=firefox_path) #creating instance of firefox weddriver
        else:
            if self.browser == 'chrome':
                chrome_path = self.config['path']['ChromePathMAC'] #path of your local chrome driver
                self.driver = webdriver.Chrome(chrome_path)  #creating instance of chrome weddriver
            else:
                firefox_path = self.config['path']['FirefoxPathMAC'] #path of your local firefox driver
                self.driver = webdriver.Firefox(executable_path=firefox_path) #creating instance of firefox weddriver
        # navigate to the gmail page
        self.driver.get(self.config['login']['BaseUrl'])

    def test_Case1_1(self):
        """TC_001_01 “Verify user is able to "Login" with valid credentials"""
       
        #enter email
        username_field = self.driver.find_element_by_id(self.config['elements']['Email'])
        username_field.send_keys(self.config['input']['Email'])
        #click on next button
        next_button = self.driver.find_element_by_xpath(self.config['xpath']['NextButton'])
        next_button.click()
        time.sleep(int(self.config['sleepTime']['LongWait']))#wait for 3 sec
        #enterpassword
        password_field = self.driver.find_element_by_xpath(self.config['xpath']['Password'])
        password_field.send_keys(self.password)
        #click on next button
        next_button = self.driver.find_element_by_xpath(self.config['xpath']['NextButton'])
        next_button.click()
        time.sleep(int(self.config['sleepTime']['LongLongWait'])) #wait for 5 sec
        #validation if user login or not
        #to validate inbox tab
        text_msg = self.driver.find_element_by_xpath(self.config['xpath']['VerifyLoginAcc']).text
        self.assertIn(self.config['text']['VerifyLoginAcc'],text_msg)

    def test_Case1_2(self):
        """TC_001_02 “Verify if a user cannot login with a valid email and an invalid password"""
       
        #enter email
        username_field = self.driver.find_element_by_id(self.config['elements']['Email'])
        username_field.send_keys(self.config['input']['Email'])
        #click on next button
        next_button = self.driver.find_element_by_xpath(self.config['xpath']['NextButton'])
        next_button.click()
        time.sleep(int(self.config['sleepTime']['LongWait']))
        #enterpassword
        password_field = self.driver.find_element_by_xpath(self.config['xpath']['Password'])
        password_field.send_keys(self.wrong_password)
        #click on next button
        next_button = self.driver.find_element_by_xpath(self.config['xpath']['NextButton'])
        next_button.click()
        time.sleep(int(self.config['sleepTime']['LongLongWait'])) #wait for 3 sec
        #validation of incorrect password
        text_msg = self.driver.find_element_by_xpath(self.config['xpath']['WrongPasswordText']).text
        self.assertIn(self.config['text']['WrongPasswordText'],text_msg)

    def test_Case1_3(self):
        """TC_001_03 “Verify if a user cannot login with a invalid email"""
       
        #enter email
        username_field = self.driver.find_element_by_id(self.config['elements']['Email'])
        username_field.send_keys(self.config['input']['IncorrectEmail'])
        #click on next button
        next_button = self.driver.find_element_by_xpath(self.config['xpath']['NextButton'])
        next_button.click()
        time.sleep(int(self.config['sleepTime']['LongLongWait']))#wait for 3 sec
        #validation of incorrect email
        text_msg = self.driver.find_element_by_xpath(self.config['xpath']['WrongEmailText']).text
        self.assertIn(self.config['text']['WrongEmailText'],text_msg)

    def tearDown(self):
        #closing the browser session
        self.driver.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('browser')
    parser.add_argument('unittest_args', nargs='*')

    args = parser.parse_args()
    # Now set the sys.argv to the unittest_args (leaving sys.argv[0] alone)
    sys.argv[1:] = args.unittest_args
    unittest.main(warnings='ignore')
