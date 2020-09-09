
#Ex.3


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com//')

cart = driver.find_element(By.XPATH,"//a[@id='nav-cart']")
cart.click()


empty_cart= driver.find_element(By.XPATH,"//div[@class='a-row sc-your-amazon-cart-is-empty']//h2")





assert 'Your Amazon Cart is empty' in empty_cart.text, \
    f'Expected Your Amazon Cart is empty, but got {empty_cart.text}'




driver.quit()

