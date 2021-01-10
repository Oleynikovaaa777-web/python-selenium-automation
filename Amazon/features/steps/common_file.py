from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.ID, 'nav-search-submit-text')

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    context.wait.until(EC.title_contains('Amazon'))



@when ('Input {search_word} into search field')
def input_search_word(context, search_word):
        # search = context.driver.find_element(*SEARCH_FIELD)
        search = context.wait.until(EC.visibility_of_element_located(SEARCH_FIELD))
        search.clear()
        search.send_keys(search_word)




@when ('Click on search button')
def click_search(context):
    search_button = context.wait.until(EC.visibility_of_element_located(SEARCH_BUTTON))
    search_button.click()


