# Reference from Doubao
import string

def check_name(name):
    # TODO: implement this function
    # no leading and trailing spaces
    if name.strip() != name: 
        return False
    
    # all printable characters
    if all(c in string.printable for c in name): 
        # Unicode emoji range
        emoji_ranges = [
            ('\U0001F600', '\U0001F64F'),
            ('\U0001F300', '\U0001F5FF'),
            ('\U0001F680', '\U0001F6FF'),
            ('\U0001F1E0', '\U0001F1FF'),
            ('\u2600', '\u26FF'),
            ('\u2700', '\u27BF')
        ]
        
        for start, end in emoji_ranges:
            if any(start <= c <= end for c in name):
                return False
        return True
    return False
    
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