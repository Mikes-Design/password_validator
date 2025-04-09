#function to check if password has lowercase letters
    #Check for lowercase letters
    #Return Truse/False and message

def check_lower(passwrd: str):
    for char in passwrd:
        if char.islower():
            print("Password meets lowercase requirment!")
            return True
        
    print("Password must have at least one lowercase letter.")
    return False