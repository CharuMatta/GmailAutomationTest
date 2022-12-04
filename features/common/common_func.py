import os,sys,platform
import configparser
from selenium import webdriver
 
config = configparser.ConfigParser(interpolation=None)
config.read('./data/config.ini')
setup_config = configparser.ConfigParser(interpolation=None)
setup_config.read('./features/setup.ini')
browser = setup_config['enviornment']['Browser']

def setup():
    if platform.system() == 'Windows':
        if browser == 'chrome':
            chrome_path = config['path']['ChromePathWindow'] #path of your local chrome driver
            driver = webdriver.Chrome(chrome_path) #creating instance of chrome weddriver
        else:
            firefox_path = config['path']['FirefoxPathWindow'] #path of your local firefox driver
            driver = webdriver.Firefox(executable_path=firefox_path) #creating instance of firefox weddriver
    elif platform.system() == 'Linux':
        if browser == 'chrome':
            chrome_path = config['path']['ChromePathLinux'] #path of your local chrome driver
            driver = webdriver.Chrome(chrome_path)  #creating instance of chrome weddriver
        else:
            firefox_path = config['path']['FirefoxPathMAC'] #path of your local firefox driver
            driver = webdriver.Firefox(executable_path=firefox_path) #creating instance of firefox weddriver
    else:
        if browser == 'chrome':
            chrome_path = config['path']['ChromePathMAC'] #path of your local chrome driver
            driver = webdriver.Chrome(chrome_path)  #creating instance of chrome weddriver
        else:
            firefox_path = config['path']['FirefoxPathMAC'] #path of your local firefox driver
            driver = webdriver.Firefox(executable_path=firefox_path)
    return driver,config

def tear_down(driver):
    driver.close()