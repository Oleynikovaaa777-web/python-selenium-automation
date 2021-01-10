from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select



MENU = (By.ID,'nav-hamburger-menu')

ITEMS = (By.XPATH,"//div[@id='hmenu-content']//ul[contains(@class, 'hmenu-visible')]//div[contains(@class, 'hmenu-item')][contains(@class, 'hmenu-title')]")





@when('Click on menu')
def click_menu(context):
    menu = context.wait.until(EC.visibility_of_element_located(MENU))
    menu.click()
    context.driver.execute_script('prompt(\'Hello!\')')
    sleep(4)
    alert = context.driver.switch_to.alert

    # alert.dismiss()
    alert.send_keys('dasdas')
    alert.accept()
    sleep(2)
    Select(context.driver.find_element(By.ID, 'searchDropdownBox'))
    for item in select.options:
        print(item.text)



@then('Get all items')
def get_items(context):
    all_items = context.driver.find_elements(*ITEMS)
    print(len(all_items))


