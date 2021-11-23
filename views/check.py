import re

def password_match_string(password: str):
    if re.findall("[a-zA-Z]+", password):
        return True
    return False

def password_match_int(password):
    if re.findall("[0-9]+", password):
        return True
    return False

def password_match_special(password):
    if re.findall("[`~!@#$%^&*(),<.>/?]+", password):
        return True
    return False

