
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
  
# Replace below path with the absolute path 
# to chromedriver in your computer 
'''driver = webdriver.Chrome('/usr/bin/chromedriver')
options = webdriver.ChromeOptions() 
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')'''

'''
options = webdriver.ChromeOptions()
options.binary_location='/usr/bin/google-chrome-stable'
'''

driver = webdriver.Chrome('/usr/bin/chromedriver')
options.add_argument('window-size={}x{}'.format(*driver.window_size))                                                                                                                                                                                                                                                                          


driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver = driver, timeout = 600)

name = input('Enter the name of the user: ')
msg = input('Enter your message : ')
count = int(input('enter count : '))

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
 
msg_box = driver.find_element_by_class_name('_2S1VP')
msg += '\n this is a system generated message'

for i in range(count):
    msg_box.send_keys(msg)
    #button = driver.find_element_by_class_name('_2lkdt')
    #button.click()
  

