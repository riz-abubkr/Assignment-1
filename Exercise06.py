 #Brute Force Attack
# Define the correct password
correct_password = "12345"

# Using a while loop to repeatedly ask the user for the password until the correct one is entered.
while True:
    # Ask the user to input the password
    entered_password = input("Please enter the password: ")
    
   #Output an appropriate message when the correct password is entered.
    if entered_password == correct_password:
        print("Access granted. Correct password entered.")
        break  
    else:
        print("Incorrect password. Please try again.")

        #ADVANCED REQUIRMENTS
max_attempts = 5
attempts = 0
while attempts < max_attempts:
    
    entered_password = input("Please enter the password: ")
    if entered_password == correct_password:
        print("Access granted. Correct password entered.")
        break  
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempts left.")
        else:
            print("Incorrect password. Authorities have been alerted.")

