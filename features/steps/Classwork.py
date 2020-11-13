from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.ID, 'nav-search-submit-text')
LEGO_HARRY = (By.CSS_SELECTOR, '#anonCarousel1 .a-section .a-size-mini .a-link-normal')
ADD_TO_CART = (By.ID, 'add-to-cart-button')
FIRST_ITEM = (By.XPATH, "//div[contains(@class,'s-result-list')]/div[@data-asin!=''][1]")
RESULT = (By.XPATH, "//span[@id='productTitle']")
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
    sleep(1)

    context.driver.find_element(*FIRST_ITEM).click()
    sleep(1)

@then('Check in title o first item will be lego text')
def contains_lego(context):
    res = context.driver.find_element(*RESULT).text
    assert 'LEGO' in res, "Expected word '{}' in message, but got '{}'".format('LEGO', res)

