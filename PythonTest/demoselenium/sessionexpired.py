from selenium import  webdriver

driver = webdriver.Chrome(executable_path='D:\Automation Testing\geckodriver.exe')

driver.get('http://paymentb.gseb.org/Student/StudentReport.aspx')
print(driver.title)
print(driver.current_url)


driver.find_element_by_name("txtUser").send_keys("98.0999")
driver.find_element_by_name("txtPass").send_keys("DCf14rhy")


