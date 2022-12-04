#Installation
For Windows:- #please install python3 and add python3 path to system path

For Mac:-#please install python3

For Linux:- Install Python3- sudo apt install python3, 
   Now type python, if you getting python-not found.
   Type- sudo apt-get install python-is-python3

pip3 install -r requirements.txt

#Introduction

Credential folder:-

   credentials.json:- This file is the credential for google Api which we are using "send_email_api.py" file

Data folder:-

   config.ini:- This file contains all the variable which is need for test cases.

      Note: Currently this test cases using firefox,chrome for testing. We are passing broswer dynimacally from command line. We can add new browser anytime.

Drivers folder:-
   contain firefox, chrome drivers

Features folder:-

   setup.ini:- This file contain browser, in which you want to run(this file is specifically for BDD test case environment)

   send_email.feature:- This file contain test scenarios in BDD

   common-

      common_func.py:- This script have all the common function which is need for BDD test case.

   steps:

      todo_steps.py:- This script run all the BDD test cases

   #To run:-

      cd automation_test

      behave **/send_email.feature

Test folder:

   login.py:- This script will validate user login to Gmail

   send_email.py:- This script will check scenario of sending an email using UI(Selenium) functionality.

   send_email_api.py:- This script will check scenario of sending an email using API

   #To run:-
      cd automation_test

      python3 test/login.py browser_name
      For Example:-

         To run login.py- python3  test/login.py chrome

         To run login.py- python3 test/login.py firefox

         To run send_email.py- python3 test/send_email.py chrome

         To run send_email.py- python3 test/send_email.py firefox

      To run send_email_api.py- python3 test/send_email_api.py

Test Cases.xlsx:- This ifile contains all the scenario for test folder

Note:- Using .env file for passwords.

Note:- There is a video of working test cases with the name-automation_video 


