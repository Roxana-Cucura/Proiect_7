Feature: Jules forgot password tests

  Background:
    Given sign_in: I am a user on Jules Sign In Page


  #@jules
  Scenario: Wrong email validation message
    When sign_in: I click forgot password link
    When forgot_password: I set my email "abcd"
    Then forgot_password: I verify email validation is correct


