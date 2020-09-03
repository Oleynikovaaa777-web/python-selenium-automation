from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.ebay.com/')



search = driver.find_element(By.XPATH, '//input[@id="gh-ac"]')
search.clear()
search.send_keys('iPhone')
search_button = driver.find_element(By.XPATH, '//input[@id="gh-btn"]')
search_button.click()

sleep(5)





# login = driver.find_element(By.XPATH,'//span[@id="gh-ug"]//a[text()="Sign in"]')




# login.click()



# wait for 4 sec
sleep(4)



driver.quit()