import string
def check_pwd(num):
    if len(num) < 8 or len(num) > 20:
        return False
    if num.isupper():
        return False
    return True