# from selenium.webdriver.common.by import By
from behave import given, when, then
# from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



@then('Can show current window')
def current_window(context):
    print(context.driver.current_window_handle)
    context.driver.execute_script("window.open('');")
    # ActionChains(context.driver).key_down(Keys.COMMAND).send_keys('t').key_up(Keys.COMMAND).perform()
    # context.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    # You can use (Keys.CONTROL + 't') on other OSs
    windows = context.driver.window_handles
    print(windows)

