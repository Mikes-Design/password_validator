
mikes test branch

# Password Validator Functions



#imports
import string

#variable that uses the string import for special characters
special_char = string.punctuation




 #function to check if password is between 8-16 characters
    # Check if password length is between 8-16 characters
    # Return True/False and message

def check_length(passwrd: str):

    if len(passwrd) >= 8 and len(passwrd) <= 16:
        print("Password Length is good!")
        return True
    else:
        print("Password length must be 8-16 characters long.")
        return False


#function to check if password has uppercase letters
    # Check for uppercase letters
    # Return True/False and message


def check_upper(passwrd: str):
    for char in passwrd:
        if char.isupper():
            print("Password meets uppercase requirement!")
            return True
    
    print("Password must have at least one uppercase.")
    return False


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
        
    
#function to check if password has at least one number
    # Check for at least one number
    # Return True/False and message

def check_number(passwrd: str): 

    for char in passwrd:
        if char.isdigit(): 
            print("Password meets number requirement!")
            return True

   
    print("Password must have at least one number.")
    return False


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



password = input("please enter a password: ")
check_special(password)



#function to check if password has forbidden phrases
    # Check for forbidden phrases (pass, qwerty, 123)
    # Return True/False and message

#function to check if all validations are True
    # Call all check functions
    # Combine results
    # Return overall validation result and messages

#function to check for spaces
    #Check for spaces in password
    #Return True/False and message

#function to get password from user
    # Handle getting password from user
    # Return cleaned input

#function to display results
    # Format and display validation results
    # Show appropriate success/error messages

#function to ask user if they want to try again
    # Ask if user wants to try again
    # Return True/False based on response

# Main program flow
    # Main program flow
    # Loop until user quits
   

#start program