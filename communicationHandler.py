import sys
import logging
import telepot
import os, psutil


logger = logging.getLogger(__name__)
#<--SET-THE-LOG-LEVEL-TO-DEBUG-->
logger.setLevel(logging.DEBUG)

#<----CREATE-FILE-HANDLERS-FOR-EACH-LOG-LEVEL---->
error_handler = logging.FileHandler('error.log')
debug_handler = logging.FileHandler('debug.log')
info_handler = logging.FileHandler('info.log')
# Set the log levels for each handler
error_handler.setLevel(logging.ERROR)
debug_handler.setLevel(logging.DEBUG)
info_handler.setLevel(logging.INFO)
# Create formatters for the log messages
error_formatter = logging.Formatter('%(asctime)s - %(message)s')
debug_formatter = logging.Formatter('%(asctime)s  - %(message)s')
info_formatter = logging.Formatter('%(asctime)s - %(message)s')
# Add the formatters to the handlers
error_handler.setFormatter(error_formatter)
debug_handler.setFormatter(debug_formatter)
info_handler.setFormatter(info_formatter)
# Add the handlers to the logger
logger.addHandler(error_handler)
logger.addHandler(debug_handler)
logger.addHandler(info_handler)


#<---------------------CUSTOM-DEBUG-FILTER--------------------->
class CustomFilter(logging.Filter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.levels_to_exclude = [logging.INFO, logging.ERROR]
    def filter(self, record):
        return record.levelno not in self.levels_to_exclude

custom_filter = CustomFilter()
debug_handler.addFilter(custom_filter)


#<-----------------CUSTOM-INFO-FILTER----------------->
class InfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno != logging.ERROR

info_filter = InfoFilter()
info_handler.addFilter(info_filter)



#<-------------------------CUSTOM-EXCEPTION-HOOK------------------------->
def log_exceptions(type, value, traceback):
    logger.error("Uncaught exception", exc_info=(type, value, traceback))
sys.excepthook=log_exceptions


#<--------------------TELEGRAM-COMMUNICATION-SETUP-------------------->
user_id = 1903052290
admin_com_bot_token = '5383795528:AAGNZYif6FcA1XAhbeTh_IfdH-4FvbG4IVw'
admin_com = telepot.Bot(admin_com_bot_token)


#<------------------------------------------------NON-SYSTEM-INITIATED-MESSAGE----------------------------------------------->
def com(msg, typ='INFO', log=True, logfile='mainLOG.log', contact_admin=False, contact_client_with_id=0):
    if log == True:
        match typ:
            case 'INFO':
                logger.info(str(msg) + ' || RAM(' + str(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2) + 'MB)')
            case 'ERROR':
                logger.error(msg,exc_info=True)
                # contact_admin = True
            case 'DEBUG':
                logger.debug(msg)
                # contact_admin = True

    #--------------------TELEPOT-HANDLING--------------------#
    if contact_client_with_id != 0:
        admin_com.sendMessage(contact_client_with_id, msg)

    if contact_admin == True:
        admin_com.sendMessage(user_id, msg)



def check_link(link):
    if link[0:28] != 'https://www.linkedin.com/in/':
        return 'LINK FORMATTING ERROR [ link does not start correctly ] \nmake sure link is formated like so https://www.linkedin.com/in/ ... /'

    elif 'recent-activity' in link:
        return 'LINK FORMATTING ERROR [ remove "recent-activity" from link ] \nmake sure link is formated like so https://www.linkedin.com/in/ ... /'

    elif link[-1] != '/':
        return 'LINK FORMATTING ERROR [ links NEED to end in "/" to ensure functionality ] \nmake sure link is formated like so https://www.linkedin.com/in/ ... /'

    elif link.count('/') != 5:
        return 'LINK FORMATTING ERROR [ slash count out of range ] \nmake sure link is formated like so https://www.linkedin.com/in/ ... /'

    else:
        return True
