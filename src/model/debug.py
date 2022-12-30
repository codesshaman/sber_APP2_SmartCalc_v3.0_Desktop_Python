def check_debug():
    file = open("debug.txt")
    check = (file.read())
    check = (file.read())
    if check == 'true':
        return True
    elif check == 'false':
        return False
    else:
        return None