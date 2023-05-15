"""from driverHandler import *
import pickle
import time
from communicationHandler import *
import pandas as pd
import re
#import speedtest-cli
#PASWORD DONT DELETE!!      )Uid,+-RB,z56Xf



page_link='https://www.linkedin.com/in/thomas-reck/recent-activity/shares/'
#https://www.linkedin.com/in/patrice-louvet/recent-activity/shares/
cookie_save_name='cookieJar/cookies110423.pkl'


def checkProxy():
    driver.get('https://dnsleaktest.com/')
    time.sleep(50)


def getCookies():
    driver.get(page_link)
    time.sleep(100)
    pickle.dump( driver.get_cookies() , open(cookie_save_name,"wb"))

    driver.quit()

def injectCookies(cookieList='cookieJar/cookies110423.pkl'):
  driver.get('https://www.linkedin.com/feed/')
  with open(cookieList, 'rb') as f:
      cookies = pickle.load(f)


  for cookie in cookies:
       # adding the cookies to the session through webdriver instance
       # cookie.pop('domain',None)
       if cookie['name'] == "fcookie":
         print("\__!!! fcookie found !!!")
         continue
       if cookie['name'] == 'bcookie':
           #print("bcookie found",'og: "v=2&f3897221-234a-4efd-896e-cb24a9edaca7" ')
           continue

       driver.add_cookie(cookie)

  com('\__Cookies injected successfully')
  time.sleep(2)


def minimalInjection():
    print('rgg')



"""

#getCookies()
#injectCookies()
#checkProxy()