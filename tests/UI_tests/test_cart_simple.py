from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_cart_page_opens(driver):
    """Проверка, что страница корзины открывается и содержит заголовок 'Корзина'"""
    url = "https://ggparts.ru/cart/"

    driver.get(url)

    # Ждем появления заголовка H1 с классом page-title
    h1_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.page-title"))
    )

    # Приводим оба значения к нижнему регистру для сравнения
    assert (
        "корзина" in h1_element.text.lower()
    ), f"Ожидали 'Корзина', получили: '{h1_element.text}'"
