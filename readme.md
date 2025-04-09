Password Validator

Side Project for Data Analytics class at Code:You
Authors: Michael Sliger & Cindy Wedding

Introduction

This project aims to create a robust password validation system to ensure login security. The program will verify the strength and security of user passwords by assessing multiple parameters.

Process Overview

1. Review Instructions – Define requirements and outline the structure through pseudocode.
2. Prepare Functions – Develop key validation functions for different password rules.
3. Testing Phase – Perform rigorous testing to ensure accuracy and efficiency.
4. Implementation – Deploy the final validated system.

Password Validator Functions

Each function will validate different password security aspects:

* Check Password Length – Ensures the password is between 8-16 characters.
* Uppercase Letter Validation – Confirms at least one uppercase letter is present
* Lowercase Letter Validation – Checks for at least one lowercase letter.
* Numeric Character Validation – Requires at least one number.
* Special Character Validation – Ensures the password contains at least one special character (e.g., ).
* Forbidden Phrase Check – Prevents weak passwords (e.g., “password,” “qwerty,” “123”).
* Whitespace Validation – Ensures no spaces are included in the password.
* Comprehensive Validation – Combines all checks and returns overall pass/fail status.
* User Input Handling – Retrieves password from the user securely.
* Result Display – Presents validation outcomes and suggestions for improvement.
* Retry Option – Allows users to reattempt password creation if validation fails.

Main Program Flow

1. Continuously prompt users to enter a password.
2. Run all validation functions sequentially.
3. Provide feedback on failed validation points.
4. Offer users the chance to correct errors and try again.
5. Exit once a valid password is successfully created.

