from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import time
import pickle
from communicationHandler import *


class DRIVER():
    def __init__(self):
        self.options = Options()
        self.service = Service(executable_path=ChromeDriverManager().install())
        self.default_page_link = 'https://www.linkedin.com/feed/'
        self.cookie_save_name = 'cookieJar/cookies110423.pkl'

    def add_option(self,arg1,arg2=None,experimental=False):
        if experimental == False : self.options.add_argument(arg1)
        else: self.options.add_experimental_option(arg1,arg2)

    def set_standard_options(self):
        self.options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        self.add_option("--no-sandbox")
        self.add_option("--disable-web-security")
        self.add_option("-headless")
        self.add_option("--window-size=1000,1300")
        self.add_option("excludeSwitches", ["enable-automation"],experimental=True)
        self.add_option('useAutomationExtension', False,experimental=True)
        self.add_option('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')
        self.add_option("--disable-dev-shm-usage")
        self.add_option("--disable-web-security")
        self.add_option("--allow-running-insecure-content")
        self.add_option("--disable-setuid-sandbox")
        self.add_option("--disable-extensions")
        self.add_option("--disable-popup-blocking")
        self.add_option("--dns-prefetch-disable")

    def start(self):
        self.driver = webdriver.Chrome(options=self.options, service=self.service)

    def stop(self):
        self.driver.quit()



    def checkProxy(self):
        self.driver.get('https://dnsleaktest.com/')
        time.sleep(50)

    def getCookies(self):
        self.driver.get(self.default_page_link)
        time.sleep(120)
        pickle.dump(self.driver.get_cookies(), open(f'cookieJar/{self.cookie_save_name}', "wb"))

        self.driver.quit()

    def injectCookies(self):
        self.driver.get(self.default_page_link)
        with open(self.cookie_save_name, 'rb') as f:
            cookies = pickle.load(f)

        for cookie in cookies:
            # adding the cookies to the session through webself.driver instance
            # cookie.pop('domain',None)
            if cookie['name'] == "fcookie":
                print("\__!!! fcookie found !!!")
                continue
            if cookie['name'] == 'bcookie':
                # print("bcookie found",'og: "v=2&f3897221-234a-4efd-896e-cb24a9edaca7" ')
                continue

            self.driver.add_cookie(cookie)

        com('\__Cookies injected successfully')
        time.sleep(1)




"""

x = DRIVER()
x.set_standard_options()
x.start()
driver = x.driver

#CODE HERE

x.stop()

"""








"""from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#
from webdriver_manager.chrome import ChromeDriverManager
import os
from communicationHandler import *
import random
from selenium.webdriver.common.by import By

#)Uid,+-RB,z56Xf



#service = Service(executable_path=os.environ.get('CHROMEDRIVER_PATH')) #HEROKU
service = Service(executable_path=ChromeDriverManager().install()) #if mode == 'LOCAL' else Service(os.environ.get('CHROMEDRIVER_PATH'))

options = Options()
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
#ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
#options.add_argument(f'user-agent={ua}')
options.add_argument("-headless")
#options.add_argument("--window-size={},{}".format(random.randint(1081,1082),random.randint(1079,1080)))
options.add_argument("--window-size=1000,1300")
#options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-web-security")
options.add_argument("--allow-running-insecure-content")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--disable-extensions")
options.add_argument("--disable-popup-blocking")
options.add_argument("--dns-prefetch-disable")

#DISABLE FOR COOKE FETCHING

options.add_argument('--blink-settings=imagesEnabled=false')
options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

#MOBILE MODE

mobile_emulation = {
    "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
}
options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(options=options, service=service)#,desired_capabilities=capabilities)
#driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
"""