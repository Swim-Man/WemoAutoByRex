#=================================================
# -*- coding: UTF-8 -*- 
# Author      : Rex Chung
# Create Date : 2018/08/21(Tue.)
# Rex code History: Write finish of rule function on 8/14 (Tue.)
# Rex code History: Change Script to unnitest  framework on 8/20 (Mon.)
# Rex code History: can show HTML report on 8/21 (Tue.)
#=================================================


from appium import webdriver
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import datetime
import HTMLTestRunner

class appium_test(unittest.TestCase):
    @classmethod
    def test_1_X(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = '039f7a6d251a2ad7'
        desired_caps['appPackage'] = 'com.belkin.wemoandroid'
        desired_caps['appActivity'] = 'com.belkin.activity.MainActivity'
        desired_caps['unicodeKeyboard']= True
        desired_caps['resetKeyboard'] = True #keyboard will not show
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)  
        print('test sleep  on')     
        #time.sleep(5)
        
    @classmethod
    def test_2_X(self):
	   '''use id/content-desc/ text / to identify webelement'''
       #driver.find_element_by_id('').click()
	   #driver.find_element_by_accessibility_id('').click()
	   #driver.find_element_by_xpath("//*[contains(@text, 'Set time')]")
	   '''if can't click(),can use tap , method as following'''
	   # Setdate =  driver.find_element_by_xpath("//*[contains(@text, 'Set date')]")
	   #Setdatex = Setdate.location.get('x') 
       #Setdatey = Setdate.location.get('y')
       #print('Setdate-x:',Setdatex)
       #print('Setdate-y:',Setdatey)
	   #driver.tap([(Settimex,Settimey)],100)
	   '''you can start activity'''
	   #driver.start_activity("com.belkin.wemoandroid", "com.belkin.activity.MainActivity")
driver.tap([(Setdatex,Setdatey)],100)
    def test_3_X(self):        

    def test_4_X(self):
       
    def test_5_X(self):
       
   
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(appium_test)
    unittest.TextTestRunner(verbosity=2).run(suite)
    #f = open('report.html','wb')#打開一個保存結果的html文檔
    #runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='測試報告',description='測試情況')#生成執行用例的對象
    #runner.run(suite)#運行
    
    