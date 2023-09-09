import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_find_button_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(7)
    
    # находим кнопку и проверяем
    assert browser.find_elements(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket"), 'Нет элемента'
            
if __name__ == "__main__":
    pytest.main()