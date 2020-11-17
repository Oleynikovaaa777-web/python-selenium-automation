from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



HOME = (By.CSS_SELECTOR, '.hl-cat-nav__active')




@given('Open Ebay page')
def open_ebay(context):
    context.driver.get('https://www.ebay.com/')


@then('Home video link has active class')
def check_active_class(context):
    home_link = context.driver.find_element(*HOME)
    home_link_classes = home_link.get_attribute("class")
    assert 'hl-cat-nav__active' in home_link_classes


