from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.CSS_SELECTOR, "input#user-name")
username.clear()
username.send_keys("standard_user")

password = driver.find_element(By.CSS_SELECTOR, "#password")
password.clear()
password.send_keys("secret_sauce")

driver.find_element(By.CSS_SELECTOR, "#login-button").click()

driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
driver.find_element(By.CSS_SELECTOR, "#checkout").click()

first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
first_name.clear()
first_name.send_keys("Иван")

last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
last_name.clear()
last_name.send_keys("Кушеев")

zip = driver.find_element(By.CSS_SELECTOR, "#postal-code")
zip.clear()
zip.send_keys("123456")

driver.find_element(By.CSS_SELECTOR, "#continue").click()

txt = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
print(f'Итоговая сумма: {txt}')

total = "Total: $58.29"

assert total in txt, f"Ошибка: Ожидалась сумма {total}, но получена {txt}"

driver.quit()