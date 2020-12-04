from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@given('Open Ebay page')
def open_ebay(context):
    context.driver.get('https://www.ebay.com/')