import getpass

while True:
    # Prompt the user for a password without echoing
    password = getpass.getpass("Enter your password: ")
    
    # Display the entered password
    print(f"You entered: {password}")
    
    # Ask if the user wants to enter another password
    response = input("Do you want to enter another password? (yes/no): ").strip().lower()
    
    if response != 'yes':
        print("Exiting the program.")
        break