from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

links = ("http://suninjuly.github.io/selects1.html", "http://suninjuly.github.io/selects2.html")
for link in links:
    try: 
        browser = webdriver.Chrome()
        browser.get(link)

        x1 = browser.find_element(By.ID, "num1").text
        x2 = browser.find_element(By.ID, "num2").text
        y = int(x1) + int(x2)
        
        Select(browser.find_element(By.ID, "dropdown")).select_by_visible_text('%s' % y)
        button = browser.find_element(By.CLASS_NAME, "btn.btn-default").click()
        
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
 