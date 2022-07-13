#There are 2 type of waits
#Implicit Waits
#Explicit Waits
# Pause The test for some seconds using Time Class

import time
import typing

from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\Automation Testing\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.get()
