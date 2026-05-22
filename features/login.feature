Feature: Login functionality

Scenario: Successful login with valid credentials

  Given user is on login page
  When user enters valid username and password
  And clicks login button
  Then user should be redirected to secure page