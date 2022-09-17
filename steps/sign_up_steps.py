from behave import *


@given('sign_in: I am a user on Jules sign in page')
def step_impl(context):
    context.sign_in_page.navigate_to_sign_in_page()


@when('sign_up: I click on Personal button')
def impl_steps(context):
    context.sign_up_page.click_personal_button()


@when('sign_up: I click on Continue button')
def impl_steps(context):
    context.sign_up_page.click_continue_btn()


@when('sign_up: I set my first name "{first_name}"')
def impl_steps(context, first_name):
    context.sign_up_page.set_first_name(first_name)


@when('sign_up: I set my last name "{last_name}"')
def impl_steps(context, last_name):
    context.sign_up_page.set_last_name(last_name)


@when('sign_up: I set my email "{sign_up_email}"')
def impl_steps(context, sign_up_email):
    context.sign_up_page.set_email(sign_up_email)


@then('sign_up: I see the email validation error message')
def impl_steps(context):
    context.sign_up_page.verify_email_error_msg_is_displayed()


@then('sign_up: I dont see the email validation message')
def step_impl(context):
    context.sign_up_page.verify_email_error_msg_is_gone()


@then('sign_up: I verify URL link "{url}"')
def step_impl(context, url):
    context.base_page.verify_current_url(url)
