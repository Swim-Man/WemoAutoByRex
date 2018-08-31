import numpy as np
import cv2
import aircv as ac 
from appium import webdriver
import time
import unittest
from selenium.webdriver.common import desired_capabilities

img = cv2.imread('D:\\GitRex\\pic.png')
x = type(img)
print(x)
y = img.shape
print(y)
#cv2.imshow('My Image', img) # open the picture
#cv2.waitKey(0)
#cv2.destroyAllWindows() 

img2 = cv2.imread('D:\\GitRex\\set.png')
y2 = img.shape
print(y2)

pos = ac.find_template(img, img2)
print (pos)
   
        
        
         
        
        