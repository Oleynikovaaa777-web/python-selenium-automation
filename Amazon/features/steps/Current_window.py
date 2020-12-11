from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


GIFT_CARDS = (By.XPATH, '//a[@data-csa-c-slot-id="nav_cs_0"]')

BEST_SELLERS = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_bestsellers"]')

PRIME = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_primelink_nonmember"]')

CUSTOMER_SERVICE = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_customerservice"]')

NEW_RELEASES = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_newreleases"]')

FIND_A_GIFT = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_giftfinder"]')

WHOLE_FOODS = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_whole_foods_in_region"]')

BOOKS = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_books"]')

AMAZONBASICS = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_amazonbasics"]')

KINDLE_BOOKS = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_kindle_books"]')

TOYS_GAMES = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_toys"]')

FASHION = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_fashion"]')

SELL = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_sell"]')


@then('Can show current window')
def current_window(context):
    print(context.driver.current_window_handle)
    context.driver.execute_script("window.open('');")



    ActionChains(context.driver).key_down(Keys.COMMAND).send_keys('t').key_up(Keys.COMMAND).perform()

    context.driver.find_element_by_xpath('//a[@data-csa-c-slot-id="nav_cs_0"]').send_keys(Keys.CONTROL + 't')


    windows = context.driver.window_handles
    sleep(4)

    print(windows)

    ActionChains(context.driver).key_down(Keys.COMMAND).send_keys('w').key_up(Keys.COMMAND).perform()
    context.driver.find_element_by_xpath('//a[@data-csa-c-slot-id="nav_cs_0"]').send_keys(Keys.CONTROL + 'w')
    sleep(3)
    print(windows)








