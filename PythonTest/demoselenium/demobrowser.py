from selenium import webdriver

#driver = webdriver.firefox(executable_path='D:\Automation Testing\chromedriver.exe')

driver = webdriver.Chrome(executable_path='D:\Automation Testing\chromedriver.exe')  # IDE Driver to run code in to teh Internet Exploxer browser

#driver.current_url() # This method is used for Website are redirect on the current website,
# do not redirect on the 3rd party website

print(driver.get("https://demo5.gipl.in"))
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://demo5.gipl.in/Registration.aspx")
driver.minimize_window()
driver.back()

#driver.refresh()
#driver.close()







