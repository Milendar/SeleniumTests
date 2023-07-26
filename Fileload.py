from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
import time 

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    input1 = browser.find_element(By.XPATH, "//input[@placeholder='Enter first name']")
    input1.send_keys("Petrov")
    input2 = browser.find_element(By.XPATH, "//input[@placeholder='Enter last name']")
    input2.send_keys("Petr")
    input3 = browser.find_element(By.XPATH, "//input[@placeholder='Enter email']")
    input3.send_keys("Petrov@mail.com")
    input4 = browser.find_element(By.XPATH, "//input[@id='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    input4.send_keys(file_path)
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()


    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце 