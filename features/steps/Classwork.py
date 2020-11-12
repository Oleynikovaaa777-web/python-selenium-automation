from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.ID, 'nav-search-submit-text')
LEGO_HARRY = (By.CSS_SELECTOR, '#anonCarousel1 .a-section .a-size-mini .a-link-normal')
ADD_TO_CART = (By.ID, 'add-to-cart-button')
FIRST_ITEM = (By.XPATH, "//img[@alt='LEGO Super Mario Adventures with Mario Starter Course 71360 Building Kit, Interactive Set Featuring Mario, Bowser Jr. and ...']")
#######################



@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')

#
#
#
@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_FIELD)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_BUTTON).click()
    sleep(1)

@then('Choose a first item in result list')
def click_first_item(context):
    context.driver.find_element(*LEGO_HARRY).click()
    sleep(1)

@then('Check in title that first item will be lego text')
def contains_lego(context):
    context.driver.find_element(*FIRST_ITEM).click()
    sleep(1)
    assert 'lego' in FIRST_ITEM, "Expected word '{}' in message, but got '{}'".format('lego', FIRST_ITEM)





