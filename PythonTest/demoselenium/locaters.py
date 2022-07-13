import options as options
from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


options = options;
driver = webdriver.chrome(service=Service(ChromeDriverManager().install()), options=options)
print(driver.get("https://demo5.gipl.in"))
print(driver.title)

driver.maximize_window()
print(driver.current_url)
driver.get("https://demo5.gipl.in/Registration.aspx")

driver.find_element_by_name("txtFullName").send_keys("Aakashkumar dave")
driver.find_element_by_name("txtAadharCardNo").send_keys("970548881777")
driver.find_element_by_xpath("//input[@value='0']").click()
driver.find_element_by_id("txtBirthdate").send_keys("19/08/1994")
driver.find_element_by_id("txtMobileNo").send_keys("6354160364")
driver.find_element_by_id("txtEmailID").send_keys("jay.s@gipl.net")
driver.find_element_by_id("txtPassword").send_keys("Test@1234")
driver.find_element_by_id("txtConfirmPassword").send_keys("Test@1234")
driver.find_element_by_id("txtCaptcha").send_keys("6BYUHL")
driver.find_element_by_xpath("//input[@value='નોંધણી કરો']").click()


