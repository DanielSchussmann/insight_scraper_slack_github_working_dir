from scrapeHandler import *
from communicationHandler import *
from jinja2 import Template

active_channel =test_channel




try:
    result = client.conversations_history(channel=active_channel)
    conversation_history = result["messages"]
    for msg in conversation_history:
        if "client_msg_id" in msg.keys():
            if 'thread_ts' not in msg.keys():

                link = msg['text'][1:-1]
                check = check_link(link)

                if  check != True:
                    client.chat_postMessage(channel=active_channel, thread_ts=msg['ts'], text=f'{check}')
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
                        posts_in_tf=np.round(result['posts_in_tf']/12,2),
                        avg_likes=result['avg_likes'],
                        profile_redirect=link,
                        avg_comments=result['avg_comments'],
                        ttl_likes=result['ttl_likes'],
                        ttl_comments=result['ttl_comments'],
                        tables=[result['mip'].to_html(classes='data', header="true", index=False)],
                        pp_url=result['pp_url'])

                    base_output=f"{result['user_name']}'s KPI \n Follower: {result['followers']} \n Posts per week: {np.round(result['posts_in_tf']/12,2)} \n Likes(avg): {result['avg_likes']} \n Comments(avg): {result['avg_comments']} \n Post range: {result['first_post']} - {result['last_post']}"


                    file_name = 'html_saves/' + result['user_name'] + ' ' + str(datetime.datetime.now())[:10] + '.html'
                    save_html = open(file_name, "w")
                    save_html.write(render)
                    save_html.close()
                    client.files_upload(channels=active_channel,
                                        initial_comment=base_output if result['timeout'] == False
                                        else f"NOTE: Profile's post frequency is to high to ensure a stable scrape. timeout after {timeout_trigger} \n" + base_output,
                                        thread_ts=msg['ts'],
                                        file=file_name)
                    #client.chat_postMessage(channel=test_channel, thread_ts=msg['ts'], text='HELLOU')

                except  Exception as e_loop:
                    #print(e_loop, '$$| loop-except-trigger |$$')
                    client.chat_postMessage(channel=active_channel, thread_ts=msg['ts'], text=f':zap:{e_loop} \n _Check pinned messages for HELP_')

except  Exception as e_main:
    #print(e_main ,'outer-except-trigger')
    client.chat_postMessage(channel=admin_channel, text=f'~FULL FAILURE~ \n {e}')



