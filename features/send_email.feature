Feature: Test to send email 

Scenario: Test Send Email Functionlity
Given I go to gmail to login
Then I login to gmail with valid credential
When I Click on compose section
When I enter email to recipient,subject to Subject,body to text area
When I click send button
Then I should verify email has been sent