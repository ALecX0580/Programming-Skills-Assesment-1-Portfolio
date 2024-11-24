# For searching something from list

names = ["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"]

search = input("Enter the name to search: ") # Ask user to enter a name to search

corrected_search = search.capitalize() # Capitalize first letter of input

# Check if name searched is in list of names
if corrected_search in names:
    print(f"Name is found: {corrected_search}")
else:
    print("Name is not found")