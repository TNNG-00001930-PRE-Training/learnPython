import re

def check_password(password):
    if 6 <= len(password) <= 12 and re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search("[0-9]", password) and re.search("[$#@]", password):
        return True
    return False


input_password = input("Enter a sequence of passwords: ")
password_list = input_password.split(',')

valid_password = [password for password in password_list if check_password(password)]
print(','.join(valid_password))