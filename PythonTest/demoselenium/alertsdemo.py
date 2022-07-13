from selenium import webdriver

ValidateText = "option3"
driver = webdriver.Chrome(executable_path="D:\Automation Testing\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_css_selector("#name").send_keys("ValidateText")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
assert ValidateText in alerttext
alert.accept()
alert.dismiss()
alerttext = alert.text
