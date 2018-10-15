# UI automated test

This part is do for UI automated test. I use Selenium in Python3.6.5 to do automated test.

## Problem when write automated test code.

  1. Run test case which is ChromeDriver, but failed, it show a message "selenium.common.exceptions.WebDriverException: Message: *'chromedriver' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home"*
     
     ***solution***  
     (1) We can download chromedriver, put it in the project, and use following code to run chromedriver
     ```
     from selenium import webdriver
     import os
     chromedriver = "/Users/Bo/autoTest/UITest/chromedriver"
     os.environ["webdriver.chrome.driver"] = chromedriver
     driver = webdriver.Chrome(chromedriver)
     driver.get("http://www.baidu.com")
     print(driver.name)
     ```
     (2) Maybe we can config chromedriver to the PATH, eg. 
     ```
     vim ~/.bash_profile
          export PATH=$PATH:ChromeDriver目录(注意，是存放的目录，不是这个文件,就是bin的目录)
          :wq
          source ~/.bash_profile  
     ```
      *(The link is https://www.jianshu.com/p/afd552124244. I did not trying it)*