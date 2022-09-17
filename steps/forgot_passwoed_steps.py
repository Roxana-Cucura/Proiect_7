from behave import *

@when('forgot_password: I set my email "{email}"')
def step_impl(context, email):
    context.forgot_password_page.set_email(email)


@then('forgot_password: I verify email validation is correct')
def step_impl(context):
    context.forgot_password_page.verify_email_error_message()
