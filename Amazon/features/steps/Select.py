from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


ALEXA = (By.XPATH,"//select[@id='searchDropdownBox']//option[@value='search-alias=alexa-skills']")
RESULT = (By.XPATH, "//span[contains(text(),'1 result for')]")




@when('Select category Alexa Skills')
def select_alexa_skills(context):
    select = Select(context.driver.find_element(By.ID, 'searchDropdownBox'))
    alexa_skills = context.driver.find_element(*ALEXA)
    alexa_skills.click()






@then('Check the message')
def check_message_results(context):
    message_res = context.driver.find_element(*RESULT).text
    assert '1 result' in message_res



# @then('Check you got Showing results from All Departments')
# def check_results(context):



