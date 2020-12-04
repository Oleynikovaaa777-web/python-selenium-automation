from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.ID, 'nav-search-submit-text')
ADD_TO_CART = (By.ID, 'add-to-cart-button')
COMPUTER_SCREEN = (By.XPATH, "//div[contains(@class, 's-result-list')]/div[contains(@class, 's-result-item')][2]//h2/a")
POPUP = (By.ID, 'siAddCoverage-announce')









@when ('Choose first result')
def first_result(context):
    f_result = context.driver.find_element(*COMPUTER_SCREEN)
    f_result.click()
    sleep(2)





@when ('Add it to cart')
def add_to_cart(context):
    add_cart = context.driver.find_element(*ADD_TO_CART)
    add_cart.click()
    sleep(3)




@then ('Close popup if it shown')
def close_popup(context):
    close_popup_window = context.driver.find_elements(*POPUP)
    if len(close_popup_window) > 0:
        close_popup_window[0].click()














