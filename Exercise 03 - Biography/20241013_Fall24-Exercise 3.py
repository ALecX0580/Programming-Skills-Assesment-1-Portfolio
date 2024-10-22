# Collect user input for nama, hometown, and age 
name = input("Enter your name: ")
hometown = input("Enter your hometown: ")

# Collect valid age input
while True:  
    try:
        age = int(input("Enter your age: "))    # Try converting input to integer
        break                                   # Exit loop if conversion is successful
    except ValueError:
        print("Invalid input. Enter a numeric value.")  # Handle non-integer input


# Store information in dictionary
person_info = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Print information stored in dictionary
print(f"\nName: {person_info['name']}\nHometown: {person_info['hometown']}\nAge: {person_info['age']}")
