#function to check if password has uppercase letters
    # Check for uppercase letters
    # Return True/False and message


def check_upper(passwrd: str):
    for char in passwrd:
        if char.isupper():
            print("Password meets uppercase requirement.")
            return True
        else:
            print("Password must have at least one uppercase.")
            return False
