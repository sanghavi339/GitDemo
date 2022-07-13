from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='D:\Automation Testing\chromedriver.exe')

print(driver.get('https://rahulshettyacademy.com/angularpractice/'))

driver.maximize_window()

driver.find_element_by_css_selector("input[name='name']").send_keys("Hemal")
driver.find_element_by_name("email").send_keys('jay.s@gipl.net')

driver.find_element_by_id("examplaecheck1").click()

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))

dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element_by_xpath("//input[@type='submit']").click()

message = driver.find_element_by_class_name("alert-success").text

#assert "sucessfully" in message

