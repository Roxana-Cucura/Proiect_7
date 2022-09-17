Feature: sign up tests

  Background:
    Given sign_in: I am a user on Jules Sign In page

  @sign_up
  Scenario: Verify that email validation message is displayed
    When sign_in: I click on Sign Up link
    When sign_up: I click on Personal button
    When sign_up: I click on Continue button
    When sign_up: I set my first name "Roxana"
    When sign_up: I click on Continue button
    When sign_up: I set my last name "Cucura"
    When sign_up: I click on Continue button
    When sign_up: I set my email "roxana"
    Then sign_up: I see the email validation errorr message
    When sign_up: I clear my email
    When sign_up: I set my email "roxana@yahoo.com"
    When sign_up: I click on Continue button
    Then sign_up: I should land on the last step