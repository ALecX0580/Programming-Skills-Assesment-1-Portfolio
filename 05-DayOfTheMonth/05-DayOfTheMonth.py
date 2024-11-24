# Determines which month has many amount of days and if it is a leap year

def leap_year(year):
    # Solves if given year is leap year
    # A leap is a year divisible by 4, except for end of centuries years, which should be divisible by 400 to be considered leap year
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Dictionary mapping the number of months to number of days in each month
months = {
    1: 31,  #January
    2: 28,  #February
    3: 31,  #March
    4: 30,  #April
    5: 31,  #May
    6: 30,  #June
    7: 31,  #July
    8: 31,  #August
    9: 30,  #September
    10: 31, #October
    11: 30, #November
    12: 31  #December
}

# A list of month names for reference, where index correlates to given number by user
month_names = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",] 

# The program which handles for user input
try:
    year = int(input("Enter the year: ")) # Ask the user for what year

    user_month = int(input("Enter the month number ranging from 1 to 12: ")) # Ask for number correlating to the number of months

    # Confirms if what user input is within the range
    if 1 <= user_month <= 12:
        # Check if february to change for leap year
        if user_month == 2:
            if leap_year(year):
                print(f"{month_names[user_month - 1]} has 29 days")                     # February in leap year
            else:
                print(f"{month_names[user_month - 1]} has {months[user_month]} days")   # February in non-leap year
        else:
            # For other months, output number of days based on month dictionary
            print(f"{month_names[user_month - 1]} has {months[user_month]} days")
    else:
        print("Invalid month number, enter a number between 1 and 12")
except ValueError:
    print("Enter a valid number please") # Error message for non-integer input