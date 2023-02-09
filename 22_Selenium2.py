from selenium import webdriver
from selenium.webdriver.common.by import By

import time


chromedriver = 'c:/webdriver/chromedriver'
driver = webdriver.Chrome(chromedriver)

# driver.get('https://www.base64decode.org/')
# element = driver.find_element(By.CSS_SELECTOR,'#input')
# element.send_keys('python')
# button = driver.find_element(By.CSS_SELECTOR, '#submit_text')
# button.click()
# print('')

driver.get('https://www.jungle.co.kr/magazine')

element1 = driver.find_elements(By.CSS_SELECTOR,'li')
print(len(element1))

button = driver.find_element(By.CSS_SELECTOR, '#more')
button.click()
time.sleep(2)

element1 = driver.find_elements(By.CSS_SELECTOR,'li')
print(len(element1))

print('')