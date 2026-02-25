# Time Handling Module
from datetime import datetime


def get_current_time():
    """
    Get the current date and time.
    
    Returns:
        datetime: Current date and time object
    """
    return datetime.now()


def get_formatted_time():
    """
    Get the current time formatted as YYYY-MM-DD HH:MM:SS.
    
    Returns:
        str: Formatted timestamp string
    """
    current_time = get_current_time()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time