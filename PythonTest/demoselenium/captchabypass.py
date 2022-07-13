### Run Browser With Service Object
### Captcha Brpwser solver from backend

from selenium import webdriver
##from captcha_solver import CaptchaSolver

from selenium.webdriver.chrome.service import Service
s = Service('D:\chromedriver.exe')
browser = webdriver.Chrome(service=s)
driver = url='https://oas2022.guadmissions.in/Student/Login.aspx'
browser.get(driver)





