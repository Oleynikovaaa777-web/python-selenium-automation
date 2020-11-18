from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

POPULAR_ELEMENTS = (By.CSS_SELECTOR, 'li.hl-popular-destinations-element')

@when('Get all popular elements')
def get_all_elements(context):
    popular_elements = context.driver.find_elements(*POPULAR_ELEMENTS)
    print(popular_elements)

@then('Number of elements should be {number_of_elements}')
def count_elements(context, number_of_elements):
        popular_el = context.driver.find_elements(*POPULAR_ELEMENTS)
        print(len(popular_el))
        assert len(popular_el) == int(number_of_elements)

