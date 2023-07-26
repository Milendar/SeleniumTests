from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects2.html"

    
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, 'num1')
    x = x_element.text
    y_element = browser.find_element(By.ID, 'num2')
    y = y_element.text
    print(x)
    print(y)
    c = int(x) + int(y)
    print(c)
    
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(str(c))
    input1 = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    input1.click()
   
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла