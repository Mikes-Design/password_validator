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