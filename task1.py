# Reference from Doubao
def check_name(name):
    # TODO: implement this function
    if name.strip() != name:
        return False

    try:
        name.encode('ascii')
    except UnicodeEncodeError:
        return False
    return True
    
        

def check_name_len(name):
    # TODO: implement this function

    if len(name.encode('utf-8')) > 20:
        return False
    return True

def check_sid_len(sid):
    # TODO: implement this function
    sid_str = str(sid)
    
    if len(sid_str) == 10:
        if sid_str.isdigit():
            if sid_str.startswith('1155'):
                return True
    return False