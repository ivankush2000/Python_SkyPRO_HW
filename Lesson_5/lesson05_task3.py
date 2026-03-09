from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

driver.get("https://the-internet.herokuapp.com/login")

input1 = "input#username"

search_input = driver.find_element(By.CSS_SELECTOR, input1)
search_input.send_keys("tomsmith") 
sleep(1)

input2 = "input#password"
search_input = driver.find_element(By.CSS_SELECTOR, input2)
search_input.send_keys("SuperSecretPassword!") 
sleep(1)

search_input.send_keys(Keys.ENTER)
