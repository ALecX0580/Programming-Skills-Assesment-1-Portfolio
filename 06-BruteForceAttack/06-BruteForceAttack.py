# Requires the correct password and puts the amount of attempts to enter password

correct_password = "12345"  # The correct password
max_attempts = 5            # Maximum allowed attempts 
attempt = 0     # The initial amount of attempts

# Loop until maximum number of attempts is reached
while attempt < max_attempts:
        password = (input("Enter the password: ")) # Ask user for password input
        attempt = attempt + 1 # Increase attempt count

        #Check if entered password matches correct password
        if password == correct_password:
            print("You have been granted access")
            break # Exit inner loop if password is correct
        else:
            # Evaluates remaining attempts
            remaining_attempt = max_attempts - attempt
            if remaining_attempt > 0:
                print(f"Incorrect password, you have {remaining_attempt} attempts left")
            else:
                print("Maximum attempts reached, authorities have been alerted")