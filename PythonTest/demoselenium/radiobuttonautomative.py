from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\Automation Testing\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

checkboxes = driver.find_elements_by_name("checkBoxOption3")
print(checkboxes)

for checkbox in checkboxes:
    checkbox.get_attribute("checkBoxOption3")
    checkbox.click()
    assert checkbox.is_selected()

radiobtn = driver.find_elements_by_name("radioButton")
radiobtn[2].click()
assert radiobtn[2].is_selected()

