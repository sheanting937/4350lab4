# Reference from Doubao
import re

def check_name(name):
    # TODO: implement this function
    # no leading and trailing spaces
    if name.strip() != name: 
        return False
    
    # Unicode printable characters
    # no Unicode emoji
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"
                               u"\U0001F300-\U0001F5FF"
                               u"\U0001F680-\U0001F6FF"
                               u"\U0001F1E0-\U0001F1FF"
                               u"\u2600-\u26FF"
                               u"\u2700-\u27BF"
                               "]+", flags=re.UNICODE)

    if emoji_pattern.search(name):
        return False
    return True
    
def check_name_len(name):
    # TODO: implement this function
    # a maximum length of 20 bytes
    if len(name) > 20: 
        return False
    return True

def check_sid_len(sid):
    # TODO: implement this function
    # only be 10 digits (can be either integers or string of numbers, but not unicode) 
    # first 4 digits must start with 1155
    sid_str = str(sid)
    
    if len(sid_str) == 10 and sid_str.isdigit() and sid_str.startswith('1155'):
        return True
    return False