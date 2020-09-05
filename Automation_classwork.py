from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.ebay.com/')

cart = driver.find_element(By.XPATH,"//a[@class='gh-eb-li-a']")
cart.click()


empty_cart= driver.find_element(By.XPATH,"//div[@class='empty-cart']")





# assert 'You don\'t have any items in your cart' in empty_cart.text, \
#     f'Expected \'You don\'t have any items in your cart\', but got {empty_cart.text}'
# element.text - get element text
# driver.current_url
# driver.title - get current page title

driver.quit()

#
# Ex: assert signin_head.text == 'Sign-In', f'Expected \'Sign-In\', but got {signin_head.text}'