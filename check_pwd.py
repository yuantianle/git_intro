import string
def check_pwd(num):
    if len(num) < 8 or len(num) > 20:
        return False

    if num.isupper():
        return False

    if num.islower():
        return False

    flag_digit = False
    for i in num:
        if (i in string.digits):
            flag_digit = True
            break
    if flag_digit == False:
        return False

    flag_symbol = False
    for i in num:
        if (i in '~`!@#$%^&*()_+-='):
            flag_symbol = True
            break
    if flag_symbol == False:
        return False

    return True