from behave import *


@given('sign_in: I am a user on Jules Sign in page')
def step_impl(context):
    context.sign_in_page.navigate_to_sign_in_page()


@when('sign_in: I click on Sign Up link')
def step_impl(context):
    context.sign_in_page.click_sign_up_link()


@when('sign_in: I set my email "{email}"')
def step_impl(context, email):
    context.sign_in_page.set_email(email)


@when('sign_in: I set my password "{password}"')
def step_impl(context, password):
    context.sign_in_page.set_password(password)


@when('sign_in: I click login button')
def step_impl(context):
    context.sign_in_page.click_login_btn()


@when('sign_in: I click forgot password link')
def step_impl(context):
    context.sign_in_page.click_forgot_password_link()


@then('sign_in: I verify password error message exists')
def step_impl(context):
    context.sign_in_page.verify_password_error_message()


@then('sign_in: I verify that login button')
def step_impl(context):
    context.sign_in_page.verify_password_error_message()


@then('sign_in: I verify URL link "{url}"')
def step_impl(context, url):
    context.base_page.verify_current_url(url)