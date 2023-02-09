from selenium import webdriver
from selenium.webdriver.common.by import By

chromedriver = 'c:/webdriver/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get('https://crawlingstudy-dd3c9.web.app/01/')
element = driver.find_element(By.CSS_SELECTOR,'p#hello')
element1= driver.find_element(By.CSS_SELECTOR,'table')
print(element.text)
for item in element1.find_elements(By.CSS_SELECTOR,'tr'):
    print(item.text)
element2 = driver.find_element(By.CSS_SELECTOR,'a')
print(element2.get_attribute('href'))
element2.click()