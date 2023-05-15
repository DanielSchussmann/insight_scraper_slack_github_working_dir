from driverHandler import *
import re
chk_lnk= 'https://www.linkedin.com/in/frank-thelen/recent-activity/shares/'


xdrive = DRIVER()
xdrive.options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
xdrive.add_option("--no-sandbox")
xdrive.add_option("--disable-web-security")
xdrive.add_option("--window-size=1000,1300")
xdrive.add_option("excludeSwitches", ["enable-automation"],experimental=True)
xdrive.add_option('useAutomationExtension', False,experimental=True)
xdrive.add_option('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')
xdrive.add_option("--disable-dev-shm-usage")
xdrive.add_option("--disable-web-security")
xdrive.add_option("--allow-running-insecure-content")
xdrive.add_option("--disable-setuid-sandbox")
xdrive.add_option("--disable-extensions")
xdrive.add_option("--disable-popup-blocking")
xdrive.add_option("--dns-prefetch-disable")
xdrive.start()

driver = xdrive.driver

xdrive.injectCookies()

driver.get(chk_lnk)

def check_comp(name,inp,outp=None):
    try:
        check = inp
        if outp != None:
            if type(check) == outp:
                return f"{name} CONTEXT OK"
            else:
                return f"{name} CONTEXT FAIL"
        else:
            return f"{name} OK"
    except:
        return f"{name} FAIL"


print( check_comp('un_pp_parent', driver.find_element(By.CSS_SELECTOR,'.ember-view.relative') ))
print( check_comp('user name',driver.find_element(By.CSS_SELECTOR,'.ember-view.relative').find_element(By.TAG_NAME,'img').get_attribute('alt'),str ))
print( check_comp('pp_url',driver.find_element(By.CSS_SELECTOR,'.ember-view.relative').find_element(By.TAG_NAME,'img').get_attribute('src')) )
print( check_comp('followers',driver.find_element(By.CSS_SELECTOR,'.ember-view.relative').find_element(By.CSS_SELECTOR, '.pv-recent-activity-top-card__extra-info.pr4.pl4').find_elements(By.TAG_NAME,'div')[2].text,int ))
#display-flex justify-space-between t-12 t-bold t-black--light mt3
post = driver.find_elements(By.CSS_SELECTOR, '.profile-creator-shared-feed-update__container')[0]
print( check_comp('post',post))
print( check_comp('check year',driver.find_element(By.CSS_SELECTOR, '.scaffold-finite-scroll__content').text,str ))
print( check_comp('URN',post.find_element(By.CSS_SELECTOR,'.feed-shared-update-v2.feed-shared-update-v2--minimal-padding.full-height.relative.feed-shared-update-v2--e2e.artdeco-card  ').get_attribute('data-urn'),str ))
print( check_comp('date',post.find_element(By.CSS_SELECTOR,'.update-components-text-view.break-words').find_elements(By.TAG_NAME,'span')[1].get_attribute('innerHTML'),str ))

print(check_comp('likes',int(post.find_element(By.CSS_SELECTOR, '.social-details-social-counts__reactions-count').get_attribute('innerHTML').replace(',', '')),int ))
like_com_rep_wrap = post.find_elements(By.CSS_SELECTOR, 'li button span')
print(check_comp('lcr_wrap',like_com_rep_wrap))

for lcr in like_com_rep_wrap:
    text = str(lcr.get_attribute('innerHTML'))
    if re.search(r'\bcomment\b', text) or re.search(r'\bcomments\b', text):
        print(check_comp('kommentare',int(re.findall('[0-9]+', text)[0]) , int))
    elif re.search(r'\brepost\b', text) or re.search(r'\breposts\b', text):  # re.search(r'\brepost\b', lcr.text):
        print(check_comp('reposts', int(re.findall('[0-9]+', text)[0]), int ))







