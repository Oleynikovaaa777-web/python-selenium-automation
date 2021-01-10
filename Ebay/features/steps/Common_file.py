from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

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
    # search = context.driver.find_element(*SEARCH_INPUT)
    search = context.wait.until(EC.visibility_of_element_located(SEARCH_INPUT))
    search.clear()
    search.send_keys(search_word)


@when('Click on search icon')
def click_search_icon(context):
    submit = context.wait.until(EC.visibility_of_element_located(SEARCH_SUBMIT))
    submit.click()
    # context.driver.find_element(*SEARCH_SUBMIT).click()
