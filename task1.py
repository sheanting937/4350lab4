# Reference from Poe
import string

def check_name(name):
    # TODO: implement this function
    if name.strip() != name: # no leading and trailing spaces
        return False
    
    if all(c in string.printable for c in name): # all printable characters
        if any('\U0001F600' <= c <= '\U0001F64F' for c in name): # no emoji
            return False
        return True
    return False
    
def check_name_len(name):
    # TODO: implement this function
    if len(name) > 20: # a maximum length of 20 bytes
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