import unittest
import time
import configparser
import argparse
import os,sys,platform
from selenium import webdriver
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login(unittest.TestCase):
    
    def setUp(self):
        self.browser = args.browser
        """function to get all variable from config file"""
        self.config = configparser.ConfigParser(interpolation=None)
        self.config.read('./data/config.ini')
        self.password = os.environ.get('PASSWORD')
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

    def test_Case2_1(self):
        """TC_002_01 “To send email to single user"""
       
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
        #click on compose tab
        compose_tab = self.driver.find_element_by_xpath(self.config['xpath']['ComposeTab'])
        compose_tab.click()
        time.sleep(int(self.config['sleepTime']['LongLongWait'])) #wait for 5 sec
        #enterreipient
        recipients_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.config['xpath']['Recipients'])))
        recipients_field.send_keys(self.config['input']['Recipients'])
        #enterpassword
        subject_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.config['xpath']['Subject'])))
        subject_field.send_keys(self.config['input']['Subject'])
        #enterpassword
        body_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.config['xpath']['TextArea'])))
        body_field.send_keys(self.config['input']['TextArea']) 
        #click on send button
        send_button = self.driver.find_element_by_xpath(self.config['xpath']['SendButton'])
        send_button.click()
        #to verify email sent
        sent_tab = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.config['xpath']['SentTab'])))
        sent_tab.click()
        time.sleep(int(self.config['sleepTime']['LongLongWait']))

    def tearDown(self):
        #closing the browser session
        self.driver.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('browser', default='chrome')
    parser.add_argument('unittest_args', nargs='*')

    args = parser.parse_args()

    # Now set the sys.argv to the unittest_args (leaving sys.argv[0] alone)
    sys.argv[1:] = args.unittest_args
    unittest.main(warnings='ignore')
