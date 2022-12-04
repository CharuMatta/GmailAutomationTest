import time
import os
import argparse
from behave import given, when, then
from selenium import webdriver
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.common_func import setup, tear_down

password = os.environ.get('PASSWORD')
driver,config = setup()

@given('I go to gmail to login')
def base_url(Context):
    driver.get(config['login']['BaseUrl'])
    
@then('I login to gmail with valid credential')
def login(Context):
     #enter email
    username_field = driver.find_element_by_id(config['elements']['Email'])
    username_field.send_keys(config['input']['Email'])
    #click on next button
    next_button = driver.find_element_by_xpath(config['xpath']['NextButton'])
    next_button.click()
    time.sleep(int(config['sleepTime']['LongWait']))#wait for 3 sec
    #enterpassword
    password_field = driver.find_element_by_xpath(config['xpath']['Password'])
    password_field.send_keys(password)
    #click on next button
    next_button = driver.find_element_by_xpath(config['xpath']['NextButton'])
    next_button.click()

@when('I Click on compose section')
def compose_tab(Context):
    compose_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, config['xpath']['ComposeTab'])))
    # compose_tab = driver.find_element_by_xpath(config['xpath']['ComposeTab'])
    compose_tab.click()
    time.sleep(int(config['sleepTime']['LongWait']))#wait for 3 sec

@when('I enter email to recipient,subject to subject,body to text area')
def new_message(Context):
    #enterreipient
    recipients_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,config['xpath']['Recipients'])))
    recipients_field.send_keys(config['input']['Recipients'])
    #enterpassword
    subject_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,config['xpath']['Subject'])))
    subject_field.send_keys(config['input']['Subject'])
    #enterpassword
    body_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,config['xpath']['TextArea'])))
    body_field.send_keys(config['input']['TextArea'])

@when('I click send button')
def send_button(Context):
    #click on send button
    send_button = driver.find_element_by_xpath(config['xpath']['SendButton'])
    send_button.click()

@then('I should verify email has been sent')
def verify_email(Context):
    sent_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,config['xpath']['SentTab'])))
    sent_tab.click()
    time.sleep(int(config['sleepTime']['LongLongWait']))
    tear_down(driver)


