import datetime
import json
from scrapeHandler import *
#pip3 install slackclient
import slack
from communicationHandler import *
import jinja2
from jinja2 import Template

client = slack.WebClient(token='xoxb-5125654014036-5146891840544-2WGECylsIlXlq00fenhF5vKy')
test_channel = 'C053PKBHDB6'
admin_channel = 'C056R2WJ3G9'


try:

    result = client.conversations_history(channel=test_channel)
    conversation_history = result["messages"]
    for msg in conversation_history:
        if "client_msg_id" in msg.keys():
            if 'thread_ts' not in msg.keys():

                link = msg['text'][1:-1]
                check = check_link(link)

                if  check != True:
                    client.chat_postMessage(channel=test_channel, thread_ts=msg['ts'], text=f'{check}')

                try:
                    #if msg['text'][0] !='h':
                    #   raise client.chat_postMessage(channel=test_channel, thread_ts=msg['ts'], text='input formatting is false')

                    print(link, type(link))

                    com('user {} searched'.format(link))
                    com('\__Scrape initiated successfully')
                    result = scarpe_and_stat(link + 'recent-activity/shares/')

                    with open('templates/webpage/results_style_in_html.html.jinja2') as file_:
                        template = Template(file_.read())

                    render = template.render(
                        title="LI_data_roundup",
                        date=' ' + str(datetime.datetime.now())[:10],
                        user_name=result['user_name'],
                        followers=result['followers'],
                        posts_in_tf=result['posts_in_tf'],
                        avg_likes=result['avg_likes'],
                        profile_redirect=link,
                        avg_comments=result['avg_comments'],
                        ttl_likes=result['ttl_likes'],
                        ttl_comments=result['ttl_comments'],
                        tables=[result['mip'].to_html(classes='data', header="true", index=False)],
                        pp_url=result['pp_url'])

                    file_name = 'html_saves/' + result['user_name'] + ' ' + str(datetime.datetime.now())[:10] + '.html'
                    save_html = open(file_name, "w")
                    save_html.write(render)
                    save_html.close()
                    client.files_upload(channels=test_channel, initial_comment=result['user_name'] + "'s KPI",thread_ts=msg['ts'],file=file_name)
                    #client.chat_postMessage(channel=test_channel, thread_ts=msg['ts'], text='HELLOU')

                except  Exception as e:
                    client.chat_postMessage(channel=test_channel, thread_ts=msg['ts'], text=f'Sooowwy >.< something went wrong \n {e}')

except  Exception as e:
    client.chat_postMessage(channel=admin_channel, text=f'~FULL FAILURE~ \n {e}')
