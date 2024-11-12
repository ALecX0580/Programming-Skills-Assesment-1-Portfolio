# Using functions(def) to determine if number is odd or even

def main(): # Main function ask user for number and checks if odd or even then prints it
    num = int(input("Enter your number: "))
    result = even_or_odd(num)
    print(result)

def even_or_odd(numval): # Determine whether given number odd or even
    if numval % 2 == 0:  # Checks if number is divisible by 2
        return f"The number {numval} is even"   # Return message for even numbers
    else:
        return f"The number {numval} is odd"    # Return message for odd numbers
    
if __name__ == "__main__":
    main() # Execute main function when script is run directly