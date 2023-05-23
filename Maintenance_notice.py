from communicationHandler import *
import time



class Channel_notice():
    def __init__(self):
        self.channel = live_channel

    def maintenance_ON(self):
        client.chat_postMessage(channel=self.channel, text=f" :bangbang: Server is under maintenance :bangbang:  ")
        time.sleep(2)
        result = client.conversations_history(channel=self.channel)
        conversation_history = result["messages"]
        hint = conversation_history[0]['ts']
        client.chat_postMessage(channel=self.channel, thread_ts=hint, text=f"I'll get back to you as soon as it is up again. :cat2: ")


    def maintenance_OFF(self):
        client.chat_postMessage(channel=self.channel, text=f" :white_check_mark: Server is back up again :white_check_mark:  ")
        time.sleep(2)
        result = client.conversations_history(channel=self.channel)
        conversation_history = result["messages"]
        hint = conversation_history[0]['ts']
        client.chat_postMessage(channel=self.channel, thread_ts=hint, text=f"I'll do my best to keep it up. :smile_cat: ")


notify = Channel_notice()
notify.channel = test_channel
notify.maintenance_ON()
#notify.maintenance_OFF()