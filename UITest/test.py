from selenium import webdriver
import os

chromedriver = "/Users/Bo/autoTest/UITest/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://www.baidu.com")
print(driver.name)
print(driver.find_element_by_id("su"))


