#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 13:18:03 2018

@author: rohit
"""
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
username = input('Enter Username:')
password = input('Enter Password:')
url = "https://www.facebook.com/"

driver = webdriver.Chrome()
driver.get(url)
print(driver.name)
print(driver.title)
print(driver.current_window_handle)
handles_list=driver.window_handles
print(driver.page_source)
driver.find_element_by_id('email').send_keys(username)
print ('Email ID Entered')
driver.find_element_by_id('pass').send_keys(password)
print ('Password Entered')
driver.find_element_by_id('loginbutton').click()
try:
    fbtn = driver.find_element_by_xpath('//*[@id="js_k"]/div/div/div[1]/div[1]/h1/a/span')
except NoSuchElementException:
    pass
driver.quit()
    
#search_field.clear()
#search_field.submit()
#driver.get("https://www.facebook.com/apoorvu")
#search_field.send_keys("VIKAS")
#search_field.send_keys(Keys.RETURN)
