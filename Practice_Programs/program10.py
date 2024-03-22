import re

def check_password(password):
    """
    Check if the password meets the specified criteria.
    
    Parameters:
    password (str): The password to be checked.
    
    Returns:
    bool: True if the password meets all criteria, False otherwise.
    """
    if 6 <= len(password) <= 12 and re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search("[0-9]", password) and re.search("[$#@]", password):
        return True
    return False

if __name__ == "__main__":
    input_password = input("Enter a sequence of passwords: ")
    password_list = input_password.split(',')

    valid_password = [password for password in password_list if check_password(password)]
    print(','.join(valid_password))