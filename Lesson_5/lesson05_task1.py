from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")

button = "button.btn.class3.btn-primary.btn-test"
press = driver.find_element(By.CSS_SELECTOR, button)
press.send_keys(Keys.ENTER)
