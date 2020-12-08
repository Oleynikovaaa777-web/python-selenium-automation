from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_ICON = (By.ID, 'nav-cart')
EMPTY_CART = (By.CSS_SELECTOR, '.sc-your-amazon-cart-is-empty h2')
SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.ID, 'nav-search-submit-text')
LEGO_HARRY = (By.CSS_SELECTOR, '#anonCarousel1 .a-section .a-size-mini .a-link-normal')
ADD_TO_CART = (By.ID, 'add-to-cart-button')
CART_ONE = (By.XPATH, "//span[@class = 'nav-cart-count nav-cart-1']")



@when('Click on Cart icon')
def click_on_cart(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(1)


@then('Verify that Cart is empty')
def cart_is_empty(context):
    result_empty = context.driver.find_element(*EMPTY_CART).text
    print('\n{}'.format(result_empty))
    assert 'empty' in result_empty, "Expected word '{}' in message, but got '{}'".format('empty', result_empty)






# @then('Choose a first item in result list')
# def click_first_item(context):
#     context.driver.find_element(*LEGO_HARRY).click()
#
#     sleep(4)

@when('Add it to cart')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()
    sleep(1)

@then('Verify that result contains 1')
def added_to_cart(context):
    result = context.driver.find_element(*CART_ONE).text
    print('\n{}'.format(result))
    assert result in '1'

