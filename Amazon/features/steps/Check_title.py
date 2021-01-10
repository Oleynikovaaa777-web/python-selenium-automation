from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC



SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.ID, 'nav-search-submit-text')
LEGO_HARRY = (By.CSS_SELECTOR, '#anonCarousel1 .a-section .a-size-mini .a-link-normal')
ADD_TO_CART = (By.ID, 'add-to-cart-button')
FIRST_ITEM = (By.XPATH, "//div[contains(@class,'s-result-list')]/div[@data-asin!=''][1]")
RESULT = (By.XPATH, "//span[@id='productTitle']")




@then('Choose first item in result list')
def click_first_item(context):
    item = context.wait.until(EC.visibility_of_element_located(FIRST_ITEM))
    item.click()



@then('Check in title first item will be lego text')
def contains_lego(context):
    # res = context.driver.find_element(*RESULT).text
    res = context.wait.until(EC.visibility_of_element_located(RESULT))
    res_text = res.text
    assert 'LEGO' in res_text, "Expected word '{}' in message, but got '{}'".format('LEGO', res_text)

