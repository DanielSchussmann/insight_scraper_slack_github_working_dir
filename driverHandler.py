from selenium import webdriver
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
"""
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
"""
#MOBILE MODE
"""
mobile_emulation = {
    "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
}
options.add_experimental_option("mobileEmulation", mobile_emulation)
"""
driver = webdriver.Chrome(options=options, service=service)#,desired_capabilities=capabilities)
#driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

