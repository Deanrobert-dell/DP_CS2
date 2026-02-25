# Time Handling Module
from datetime import datetime


def get_current_time():
   #get the currnt dat and alos time
    return datetime.now()


def get_formatted_time():
    #format it
    current_time = get_current_time()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time