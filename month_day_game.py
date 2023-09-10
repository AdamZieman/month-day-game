# month_day_game.py
# This program demonstrates the programmers understanding of arithmetic operations.
# A user inputs a numeric value for the month and day of the month. These values are
# used along side various arithmetic operations to increment and decrement a variable.

# Course: CSCI 130 (Introduction to Programming)
# Assignment: 2

# Author: Adam Zieman
# Date: February 18, 2021

def main():
    # Heading and description of the program
    print("Welcome to the Month Day Game!")
    print("==============================")
    print("Program will ask you for a month and day number.")
    print("It will not check date validity (allows Feb 30, for example.)")
    print("It will perform a series of arithmetic operations and")
    print("will print the original month and day at the end.")
    print("-------------------------------------------------------------")
    
    # User inputs a numeric value for the month and day of the month
    month = eval(input("Enter a month number (1-12): "))
    day = eval(input("Enter a day number (1-31): "))
    print()

    # Perform the algorithm in steps and print every value calculated  
    # Step 1: make a new variable holding month entered times 7
    result = month * 7
    print("Result from step 1:", result)

    # Step 2: subtract 1 from last value and save
    result = result - 1
    print("Result from step 2:", result)
    
    # Step 3: multiply last value by 13 and save
    result = result * 13
    print("Result from step 3:", result)
    
    # Step 4: add entered day to last value and save
    result = result + day
    print("Result from step 4:", result)

    # Step 5: add 3 to last value and save
    result = result + 3
    print("Result from step 5:", result)

    # Step 6: multiply last value by 11 and save
    result = result * 11
    print("Result from step 6:", result)

    # Step 7: subtract original month from last value and save
    result = result - month
    print("Result from step 7:", result)
    
    # Step 8: subtract original day from last value and save
    result = result - day
    print("Result from step 8:", result)
    
    # Step 9: divide last value by 10 and save
    result = result // 10
    print("Result from step 9:", result)
    
    # Step 10: add 11 to last value and save
    result = result + 11
    print("Result from step 10:", result)
    
    # Step 11: separate last 2 digits from number (that's the day)
    # and separate the rest of the number for the month
    original_day = result % 100
    original_month = ((result - original_day) // 100)

    # Step 12: print the calculated results
    print()
    print("Your original month was:",original_month)
    print("Your original day was:  ",original_day)

main() # Calls the main() function
