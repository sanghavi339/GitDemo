from  selenium import  webdriver


wb = webdriver.firefox(executable_path='D:\Automation Testing\geckodriver.exe')

wb.get('https://www.google.com')