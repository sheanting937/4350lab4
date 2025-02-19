# Reference from Doubao
import re

def check_name(name):
    # TODO: implement this function
    if name.strip() != name:
        return False

    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    if emoji_pattern.search(name):
        return False
    return True
    
def check_name_len(name):
    # TODO: implement this function

    if len(name) > 20:
        return False
    return True

def check_sid_len(sid):
    # TODO: implement this function
    sid_str = str(sid)
    
    if len(sid_str) == 10 and sid_str.isdigit() and sid_str.startswith('1155'):
        return True
    return False