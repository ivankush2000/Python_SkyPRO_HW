from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/dynamicid")

button = "button#df8f192e-8e13-cd5f-3f42-ca580c581e5e.btn.btn-primary"
press = driver.find_element(By.CSS_SELECTOR, button)
press.send_keys(Keys.ENTER)
