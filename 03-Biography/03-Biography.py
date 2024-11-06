# Collects user input for personal information and stores in a dictionary

# Collect user input for first nama, second name, hometown, and age 
name1 = input("Enter your first name: ")    # Ask for first name
name2 = input("Enter your second name: ")   # Ask for second name
hometown = input("Enter your hometown: ")   # Ask for hometown

# Collect valid age input
while True:  
    try:
        # Ask for age and try to convert input to integer
        age = int(input("Enter your age: "))    
        break   # Exit loop if process is successful
    except ValueError:
        # Take cares of non-integer inputs
        print("Invalid input. Enter a numeric value.")  # Handle non-integer input

# Store collected information in dictionary
person_info = {
    "name1": name1,         # Stores first name
    "name2": name2,         # Stores second name
    "hometown": hometown,   # Store hometown
    "age": age              # Store age
}

# Print information stored in dictionary
print(f"\nFirst Name: {person_info['name1']}\nSecond Name: {person_info['name2']}\nHometown: {person_info['hometown']}\nAge: {person_info['age']}")