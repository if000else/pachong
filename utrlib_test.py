# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# chrome = webdriver.Chrome('D:\scripts\chromedriver.exe')
# chrome.get('https://www.taobao.com/')
# # chrome.close()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('D:\scripts\\browserdriver\chromedriver.exe')
driver.get("https://www.baidu.com")
driver.execute_script('window.open()')
print(driver.window_handles)
driver.switch_to.window(driver.window_handles[1])
driver.get("http://www.sohu.com/")
driver.switch_to.window(driver.window_handles[0])
driver.get("http://www.sohu.com/")
driver.close()
driver.close()
# elem = driver.find_element_by_xpath("//input[@id='kw']")
# elem.clear()
# elem.send_keys('python ')
# elem.send_keys('yield')
# elem.send_keys(Keys.RETURN)
# driver.close()
