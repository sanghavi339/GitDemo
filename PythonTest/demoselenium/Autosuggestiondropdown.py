import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service('D:\Automation Testing\chromedriver.exe')
browser = webdriver.Chrome(service=s)
url='http://3.110.88.201/dropdownsPractise/'
browser.get(url)

#driver = webdriver.Chrome(executable_path="D:\Automation Testing\chromedriver.exe")
#driver.get("http://3.110.88.201/dropdownsPractise/")
#driver.find_element_by_id("autosuggest").send_keys("ind")
#time.sleep(3)

countries = url.find_element_by_css_selector("lis[Class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break
print(url.find_element_by_id("autosuggest").text())
assert url.find_element_by_id("autosuggest").get_attribute("values") == "india"





