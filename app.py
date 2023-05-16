from internal_secrets import *
from scrapeHandler import *
#pip3 install slackclient
import slack
from communicationHandler import *
from jinja2 import Template

#check if update
client = slack.WebClient(token=slack_token)

#standard_message=f'{result['posts_in_tf']}'
#f"{result['user_name']}'s KPI \n Posts count: {result['posts_in_tf']} \n Avg. Likes: {result['avg_likes']} \n Avg. Comments: {result['avg_comments']}"


timeout_message=''



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
                    continue

                try:

                    print(link, type(link))

                    com('user {} searched'.format(link))
                    com('\__Scrape initiated successfully')
                    result = scarpe_and_stat(link + 'recent-activity/all/')

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
                    client.files_upload(channels=test_channel,
                                        initial_comment=f"{result['user_name']}'s KPI \n Posts count: {result['posts_in_tf']} \n Likes(avg): {result['avg_likes']} \n Comments(avg): {result['avg_comments']}" if result['timeout'] == False
                                        else f"NOTE: Timeout after {timeout_trigger}s. This means there might be data missing! contact admin if KPI is insufficientf \n {result['user_name']}'s KPI \n Posts count: {result['posts_in_tf']} \n Likes(avg): {result['avg_likes']} \n Comments(avg): {result['avg_comments']}",
                                        thread_ts=msg['ts'],
                                        file=file_name)
                    #client.chat_postMessage(channel=test_channel, thread_ts=msg['ts'], text='HELLOU')

                except  Exception as e:
                    client.chat_postMessage(channel=test_channel, thread_ts=msg['ts'], text=f'>.< something went wrong \n {e}')
except  Exception as e:
    print(e)
    client.chat_postMessage(channel=admin_channel, text=f'~FULL FAILURE~ \n {e}')



