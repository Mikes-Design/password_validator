#function to check if password has at least one special character
    # Check for special characters
    # Return True/False and message


#this imports the string module to use the punctuation function 
import string

def check_special(passwrd: str):
    #this creates a variable that contains all the special characters
    special_char = string.punctuation
    #this checks if the password has any special characters
    for char in passwrd:
        if char in special_char:
            print("Password meets special character requirments!")
            return True
    #if the password does not have any special characters, this will print a message and return false   
    print("Password must have at least one special character.")
    return False
