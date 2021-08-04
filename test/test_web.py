from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 导入Keys


driver = webdriver.Chrome('E:/python/chromedriver')
driver.get('http://www.baidu.com')
driver.maximize_window()



