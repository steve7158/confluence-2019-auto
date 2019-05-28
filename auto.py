from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import numpy as np
import re
import time
def cleanvalue(val):
  cleanr = re.compile(r'\s')
  cleantext = re.sub(cleanr, '', val)
  return cleantext



driver=webdriver.Chrome(executable_path='./chromedriver')
driver.get('https://docs.google.com/forms/d/e/1FAIpQLScC4dqHQuVMXYiXKXPzMxjKgN1IfN9hU4UHHvQFyn4m7fZ7BA/viewform?vc=0&c=0&w=1')
print driver.title
"""
selector=driver.find_element_by_id('identifierId')
selector.send_keys(username)
selector=driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span')
selector.click()
pa.typewrite(password)
#selector=driver.find_element_by_name('password')
#selector.send_keys(password)
selector=driver.find_element_by_xpath('//*[@id="passwordNext"]/content')
selector.click()
"""
dataset=pd.read_csv('cms_scrape.csv')
name=list(dataset.iloc[:, 0].values)
n_val=[]
phone=list(dataset.iloc[:, 1].values)
# p_val=[]
office=list(dataset.iloc[:, 2].values)
# o_val=[]
email=list(dataset.iloc[:, 3].values)
# e_val=[]
for obj in name:
    print type(obj)
    print obj
    obj=obj.rstrip("\n")
    print obj
    n_val.append(obj)

# comments=list(dataset['comments'])
next=0
for next in range(60):
    
    #Name
    selector=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input')
    selector.send_keys(name[next])
    time.sleep(0.003)
    #Designation
    selector=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input')
    selector.send_keys('regular faculty')
    time.sleep(0.003)
    #University
    selector=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/input')
    selector.send_keys('Stanford University')
    time.sleep(0.003)
    #Country
    selector=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/input')
    selector.send_keys('USA')
    time.sleep(0.003)
    #Email
    selector=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[5]/div/div[2]/div/div[1]/div/div[1]/input')
    selector.send_keys(email[next])
    time.sleep(0.003)
    selector=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[6]/div/div[2]/div[1]/div[2]/textarea')
    selector.send_keys('Computer science')
    time.sleep(0.003)
    selector=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[7]/div/div[2]/div/div[1]/div/div[1]/input')
    selector.send_keys('Steve Jose')
    time.sleep(0.003)
    selector=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div/div/content/span')
    selector.click()
    time.sleep(0.003)
    selector=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[3]/a')
    selector.click()
    time.sleep(0.003)
    print "done"
