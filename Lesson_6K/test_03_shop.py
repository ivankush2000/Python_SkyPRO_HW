from selenium import webdriver
from selenium.webdriver.common.by import By

def test_shop():
    # Инициализация драйвера
    driver = webdriver.Firefox()
    try:
        driver.get("https://www.saucedemo.com/")

        # Авторизация
        username = driver.find_element(By.CSS_SELECTOR, "input#user-name")
        username.clear()
        username.send_keys("standard_user")

        password = driver.find_element(By.CSS_SELECTOR, "#password")
        password.clear()
        password.send_keys("secret_sauce")

        driver.find_element(By.CSS_SELECTOR, "#login-button").click()

        # Добавление товаров
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

        # Переход в корзину и к оформлению
        driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
        driver.find_element(By.CSS_SELECTOR, "#checkout").click()

        # Заполнение данных
        first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
        first_name.clear()
        first_name.send_keys("Иван")

        last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
        last_name.clear()
        last_name.send_keys("Кушеев")

        zip_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
        zip_code.clear()
        zip_code.send_keys("123456")

        driver.find_element(By.CSS_SELECTOR, "#continue").click()

        # Проверка итоговой суммы
        txt = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
        print(f'Итоговая сумма: {txt}')

        total = "Total: $58.29"

        assert total in txt, f"Ошибка: Ожидалась сумма {total}, но получена {txt}"
    
    finally:
        # Важно закрыть браузер даже если тест упал
        driver.quit()