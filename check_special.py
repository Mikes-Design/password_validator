#function to check if password has at least one special character
    # Check for special characters
    # Return True/False and message

def check_special(passwrd: str):

    for char in passwrd:
        if char in special_char:
            print("Password meets special character requirments!")
            return True
        
    print("Password must have at least one special character.")
    return False


