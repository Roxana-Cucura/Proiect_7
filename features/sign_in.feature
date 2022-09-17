Feature: Jules sign in tests

  Background:
    Given sign_in: I am a user on Jules Sign In Page


  #@jules
  Scenario: Verify missing password error message
    When sign_in: I set my email "abcd@gmail.com"
    When sign_in: I set my password "123"

    #When sign_in: I click login button
    Then sign_in: I verify password error message exists
    Then sign_in: I verify that Login button is displayed

    @check-url
  Scenario: Verify what is the current URL
    When sign_in: I click on Sign Up link
    Then sign_up: I verify URL link "https://jules.app/sign-up"
    When sign_up: I click on Log In link


