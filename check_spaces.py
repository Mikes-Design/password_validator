#function to check for spaces
    #Check for spaces in password
    #Return True/False and message
#1
def check_spaces(passwrd):
    if " " in passwrd:
        print("Password cannot contain spaces")
        return True
    else:
        print("Password does not contain spaces")
        return False
    

