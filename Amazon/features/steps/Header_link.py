from pprint import pprint
from behave import given, when, then
from selenium.webdriver.common.by import By

ALL_HEADER_ELEMENTS = (By.CSS_SELECTOR, '#nav-xshop .nav-a')
FIRST_HEADER_ELEMENT = (By.CSS_SELECTOR, '#nav-xshop .nav-a:first-of-type')
SECOND_HEADER_ELEMENT = (By.CSS_SELECTOR, '#nav-xshop .nav-a:nth-of-type(2)')

@when('Find all header links')
def find_all_header_links(context):
    elements = context.driver.find_elements(*ALL_HEADER_ELEMENTS)
    context.elements = elements
    # print(len(elements))
    pprint(elements)

@then('Click elements in loop')
def elements_in_loop(context):
    for link in context.elements:
        # print(link)
        link.click()
        print(context.elements)
        print(context.driver.find_elements(*ALL_HEADER_ELEMENTS))

@then('Click first link')
def click_first_link(context):
    first_element = context.driver.find_element(*FIRST_HEADER_ELEMENT)
    print(first_element)
    first_element.click()

@then('Click second link')
def click_second_link(context):
    second_element = context.driver.find_element(*SECOND_HEADER_ELEMENT)
    print(second_element)
    second_element.click()
