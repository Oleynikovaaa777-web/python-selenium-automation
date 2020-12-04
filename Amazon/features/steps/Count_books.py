from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.ID, 'nav-search-submit-text')
FANTASY_BOOK = (By.CSS_SELECTOR, 'span.celwidget div.a-section.aok-relative.s-image-fixed-height')
ALL_PRICES = (By.XPATH,
              "//div[@data-component-type='s-search-result']//div[contains(@class, 'a-spacing-top-small')]//span[contains(@class, 'a-price-whole')]")





@when('Find all prices')
def observe_all_prices(context):
    all_prices = context.driver.find_elements(*ALL_PRICES)
    print(len(all_prices))


@then('Count how many books expensive then 20$')
def count_books(context):
    all_prices = context.driver.find_elements(*ALL_PRICES)
    count = 0
    for x in all_prices:
        y = (int(x.text))
        if y > 20:
            count += 1
            print(y)
    print(count)
