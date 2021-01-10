from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

BLOG_LINK = (By.XPATH, "//div[contains(@class, 'navFooterVerticalColumn')]//a[text()='Blog']")


@when('Click blog link')
def go_to_blog_link(context):
    # blog_link = context.driver.find_element(*BLOG_LINK)
    blog_link = context.wait.until(EC.visibility_of_element_located(BLOG_LINK))
    blog_link.click()


@when('Go back')
def go_back(context):
    context.driver.back()


@when('Go forward')
def go_forward(context):
    context.driver.forward()

@then('Check current page is {expected_current_url} page')
def check_url(context, expected_current_url):
    current_url = context.driver.current_url
    print(current_url)
    assert expected_current_url.lower() in current_url.lower(), f'Expected {expected_current_url} be in {current_url}, but it\'s not there'



