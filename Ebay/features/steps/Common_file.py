from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.NAME, '_nkw')
SEARCH_SUBMIT = (By.ID, 'gh-btn')


@given('Open Ebay page')
def open_ebay(context):
    context.driver.get('https://www.ebay.com/')
    sleep(3)

@when('Open Ebay page')
def open_ebay(context):
    context.driver.get('https://www.ebay.com/')
    sleep(3)


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)

@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(3)