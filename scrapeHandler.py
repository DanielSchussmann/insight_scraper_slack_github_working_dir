import time
from driverHandler import *
import pickle
import os
import datetime
from communicationHandler import *
from stats import *
#import speedtest for checking sleep time
from cookieHandler import *
import pandas as pd
import re

post_load_speed = 3
page_load_speed = 3
timeout_trigger = 240

def scarpe_and_stat(link,bypass = False):
#-------------------------------DRIVER-SETUP-------------------------------
    xdrive = DRIVER()
    xdrive.set_standard_options()
    xdrive.start()
    driver = xdrive.driver


#-------------------------------INJECT-COOKIES-------------------------------
    xdrive.injectCookies()

#-------------------------------INJECT-COOKIES-------------------------------
    time.sleep(1)


    if bypass == True:
        driver.get(link[:-23])
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,'.pvs-list__footer-wrapper').find_element(By.TAG_NAME,'a').click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,'.artdeco-pill-choice-group.ember-view').find_elements(By.TAG_NAME,'button')[2].click()
        time.sleep(5)
    else:
        driver.get(link)
        time.sleep(3)



    un_pp_parent = driver.find_element(By.CSS_SELECTOR,'.ember-view.relative')
    user_name = un_pp_parent.find_element(By.TAG_NAME,'img').get_attribute('alt')#driver.find_element(By.CSS_SELECTOR, 'break-words.ph5.pv0').find_elements(By.TAG_NAME,'h3').text
    pp_url  = un_pp_parent.find_element(By.TAG_NAME,'img').get_attribute('src')#driver.find_element(By.CSS_SELECTOR,'.ghost-person.ember-view.pv-recent-activity-top-card__member-photo.EntityPhoto-circle-5').get_attribute('src')
    followers = driver.find_element(By.CSS_SELECTOR, '.pv-recent-activity-top-card__extra-info.pr4.pl4').find_elements(By.TAG_NAME,'div')[2].text

    #com(followers)
    com('\__Direct info collected successfully')

    driver.execute_script("document.body.style.zoom='25%'")
    global post_data,posts_itt
    post_data = []# pd.DataFrame(columns=['date','likes','comments','reposts'])
    posts_itt = []
    init_time = time.time()
    while True:
        group = driver.find_elements(By.CSS_SELECTOR, '.ember-view.occludable-update')
        com(len(group))
        if len(posts_itt) == 0:
            posts_itt.append(group[-11:-1])





        #com(len(group))
        check_yr = driver.find_element(By.CSS_SELECTOR, '.scaffold-finite-scroll__content').text #driver.find_elements(By.CSS_SELECTOR, '.ember-view.occludable-update')[-5].find_element(By.CSS_SELECTOR,'.update-components-text-view.white-space-pre-wrap.break-words').text
        #com(check_yr)

        reggex_filter = re.findall(r"\d+[hwdmy]o?", check_yr)

        com(('Reggexed time',reggex_filter))
        #check_yr = 'yr'
        #time.sleep(2)
        #posts_itt.append(group[-11:-1])
        loop_time = time.time()
        if re.search(r'\b[3-9]+mo\b', check_yr) or re.search(r'\b[1-9]+yr\b',check_yr) or loop_time > init_time + timeout_trigger:
            if loop_time > init_time + timeout_trigger:
                 timeout = True

            else:
                timeout = False
            driver.set_window_size(700, 1300)
            for x in range(0,4):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)

            posts = driver.find_elements(By.CSS_SELECTOR, '.profile-creator-shared-feed-update__container')[:-1]

            com('Len of post push ' + str(len(posts)))

            for post in posts: #posts_itt[0]: #posts[:-5]:
                try:
                    repost_check=post.find_element(By.CSS_SELECTOR,'.update-components-header__text-view')
                    com('repost')
                    continue
                except:
                    try:
                        com(post.find_elements(By.TAG_NAME, 'div')[0])
                        urn = post.find_element(By.CSS_SELECTOR,'.feed-shared-update-v2.feed-shared-update-v2--minimal-padding.full-height.relative.feed-shared-update-v2--e2e.artdeco-card  ').get_attribute('data-urn')
                        com('CURRENT URN' + str(urn))

                        pre_date =  post.find_element(By.CSS_SELECTOR,'.update-components-text-view.break-words') #re.findall(r"\d+[hwdmy]o?", post.get_attribute('innerHTML'))[0] #
                        date_wrap = pre_date.find_elements(By.TAG_NAME,'span')[1].get_attribute('innerHTML')

                        com('\_date pre: {}'.format(date_wrap))
                        if re.search(r"\d+[hwd]", date_wrap):date_wrap = 1

                        elif re.search(r"\d+[m]o?", date_wrap): date_wrap = int(re.findall(r'\d+',date_wrap)[0])

                        else: date_wrap = 999

                        com('\_date post: {}'.format(date_wrap))
                        likes, kommentare, reposts = 0, 0, 0
                        like_com_rep_wrap = post.find_elements(By.CSS_SELECTOR, 'li button span')


                        likes = int(post.find_element(By.CSS_SELECTOR,'.social-details-social-counts__reactions-count').get_attribute('innerHTML').replace(',',''))
                        com(likes)
                        for lcr in like_com_rep_wrap:
                            text = str(lcr.get_attribute('innerHTML'))
                            if re.search(r'\bcomment\b', text) or re.search(r'\bcomments\b', text):
                                com('\_comments: '+ str(text))
                                kommentare = int(re.findall('[0-9]+',text)[0])
                            elif re.search(r'\brepost\b', text) or re.search(r'\breposts\b', text): #re.search(r'\brepost\b', lcr.text):
                                reposts = int(re.findall('[0-9]+',text)[0])
                                com('\_reposts:' + str(text))
                            """else:

                                com('passed lcr value:' + lcr.get_attribute('innerHTML'))
                                likes = int(lcr.get_attribute('innerHTML').replace(',',''))"""
                    except:
                        com('Exception in post','ERROR')
                        continue




                    #share_button = post.find_element(By.CSS_SELECTOR,'.feed-shared-control-menu__trigger.artdeco-button.artdeco-button--tertiary.artdeco-button--muted.artdeco-button--1.artdeco-button--circle.artdeco-dropdown__trigger.artdeco-dropdown__trigger--placement-bottom.ember-view')

                    #com(urn)
                    #urn_el_parent = post.find_element(By.CSS_SELECTOR,'.ember-view.occludable-update')
                    #urn =  urn_el_parent.find_element()
                    #urn_parent = post.find_element(By.CSS_SELECTOR,'.feed-shared-update-v2.feed-shared-update-v2--minimal-padding.full-height.relative.feed-shared-update-v2--e2e.artdeco-card')
                    #urn = urn_parent.get_attribute('data-urn')
                    link_to_profile='https://www.linkedin.com/feed/update/{}'.format(str(urn))
                    #post_text = post.find_element(By.CSS_SELECTOR,'.update-components-text.relative.feed-shared-update-v2__commentary').text
                    post_data.append([date_wrap, likes, kommentare, reposts,link_to_profile])
                    # com(likes,date_wrap,kommentare,reposts)

                    com(link_to_profile)

            post_data = pd.DataFrame(post_data, columns=['date', 'likes', 'comments', 'reposts', 'link'])
            post_data = post_data[post_data['date']<=2]
            com("postdata reached")
            break


        try:
            driver.execute_script("window.scrollTo(0, 0);")
            com('TOP scroll OK')
            # driver.execute_script("arguments[0].scrollIntoView(true);", button
            time.sleep(2)
            com('slept')
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            com('BOT scroll OK')
            # button.click()
            time.sleep(2)
        except Exception as e1:
            com(e1,typ='ERROR')
            pass


    # full twelve months
    """
    post_data.to_csv('csvs/out_1.csv')
    stated_data = basic_stat(post_data)
    """
    post_data.to_csv('csvs/'+ user_name +'_'+str(datetime.datetime.now())[:10]+'.csv')
    #post_data = post_data[post_data['date'] <= 3]# [input_data['date']<=3]
    com(len(post_data))
    stated_data = threeMo_stat(post_data)




    results = {'user_name':user_name,'followers':followers,'pp_url':pp_url,'timeout':timeout} | stated_data


    com('\_SCRAPED successfully')
    xdrive.stop()
    return results



