# start building calculator cli version 1.0

# importing the module
import math_functions as mt

# greeting welcome message for user
print("\nWelcome to Calculator CLI v1.0!")

# helper function for pauses between action
def helper():
    input("Press Enter to return")

# helper function to get input
def get_numbers():

    while True:

        try:                # validating input
            number = float(input(f"Enter a number: "))
            return number
        
        except Exception:
            print("Sorry! Please enter a valid number.")

# helper function to get input
def get_percent():

    while True:

        try:
            per = float(input("Enter percentage(%): "))
            if per >= 0:
                return per
            else:
                print("Sorry! Please enter a positive value.")

        except Exception:
            print("Sorry! Please enter a valid value.")

# menu for basic arithmetic
def basic_menu():

    print("\n----- Basic Operations -----\n")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (x)")
    print("4. Division (/)")
    print("5. Return to previous menu")
    print("\n----------------------------")

# basic operators function
def basic_main():

    while True:
        basic_menu()

        while True:
            choice = input("\nChoose an option (1-5): ")

            if choice == "1":

                print("First number-")
                num_1 = get_numbers()          # get number 1
                print("Second number-")
                num_2 = get_numbers()          # get number 2

                result = mt.add(num_1,num_2)
                print(f"\nResult: {round(result,2)}")

                helper()
                break

            elif choice == "2":

                print("First number-")
                num_1 = get_numbers()          # get number 1
                print("Second number-")
                num_2 = get_numbers()          # get number 2

                result = mt.subtract(num_1,num_2)
                print(f"\nResult: {round(result,2)}")

                helper()
                break

            elif choice == "3":

                print("First number-")
                num_1 = get_numbers()          # get number 1
                print("Second number-")
                num_2 = get_numbers()          # get number 2

                result = mt.multiply(num_1,num_2)
                print(f"\nResult: {round(result,2)}")

                helper()
                break

            elif choice == "4":

                print("First number-")
                num_1 = get_numbers()          # get number 1
                print("Second number-")
                num_2 = get_numbers()          # get number 2
            
                try:
                    result = mt.divide(num_1,num_2)
                    print(f"\nResult: {round(result,2)}")

                except ZeroDivisionError:
                    print("Sorry! Division by zero is not possible!")

                helper()
                break

            elif choice == "5":

                print("Returning to previous menu..")
                return

            else:
                print("Sorry! Please enter a valid choice.")

# menu for advanced math
def advance_menu():

    print("\n----- Advanced Math -----\n")
    print("1. Square")
    print("2. Square root")
    print("3. Exponent")
    print("4. Return to previous menu")
    print("\n-------------------------")    

# advanced maths function
def advance_main():

    while True:

        advance_menu()

        while True:
            choice = input("\nChoose an option (1-4): ")

            if choice == "1":

                num = get_numbers()          # get number
                
                result = mt.square(num)
                print(f"\nResult: {round(result,2)}")

                helper()
                break

            elif choice == "2":

                num = get_numbers()            # get number

                result = mt.square_root(num)
                print(f"\nResult: {round(result, 2)}")

                helper()
                break

            elif choice == "3":
                
                print("First number-")
                num_1 = get_numbers()          # get number 1
                print("Second number-")
                num_2 = get_numbers()          # get number 2

                try:
                    result = mt.exponent(num_1,num_2)
                    print(f"\nResult: {round(result, 2)}")

                except OverflowError:
                    print("Sorry! The number is too large to handle!")
                
                helper()
                break

            elif choice == "4":

                print("Returning to previous menu..")
                return

            else:
                print("Sorry! Please enter a valid choice.")

# menu for percentage tools
def percent_menu():

    print("\n-------- Percentage Tools --------\n")
    print("1. Percentage of a number")
    print("2. Increase %")
    print("3. Decrease %")
    print("4. Return to previous menu")
    print("\n----------------------------------")

# percentage tools functions
def percent_main():

    while True:

        percent_menu()

        while True:
            choice = input("\nChoose an option (1-4): ")

            if choice == "1":

                num = get_numbers()          # get number
                per = get_percent()          # get percent

                result = mt.percentage(num,per)
                print(f"\n{per}% of {num} = {round(result,2)}")

                helper()
                break

            elif choice == "2":

                num = get_numbers()          # get number
                per = get_percent()          # get percent
                
                result = mt.percentage_increase(num,per)
                print(f"\n{per}% increase of {num} = {round(result,2)}")

                helper()
                break

            elif choice == "3":

                num = get_numbers()          # get number
                per = get_percent()          # get percent
                
                result = mt.percentage_decrease(num,per)
                print(f"\n{per}% decrease of {num}: {round(result,2)}")

                helper()
                break

            elif choice == "4":

                print("Returning to previous menu..")
                return

            else:
                print("Sorry! Please enter a valid choice.")

# home menu of the application
def home_menu():

    print("\n-------- Calculator --------\n")
    print("1. Basic Arithmetic")
    print("2. Advanced Math")
    print("3. Percentage Tools")
    print("4. Exit")
    print("\n----------------------------")

# main function of the application
def main():

    while True:

        home_menu()     # displaying the home menu

        while True:
            choice = input("\nEnter your choice (1-4): ")

            if choice == "1":
                basic_main()
                break

            elif choice == "2":
                advance_main()
                break
            
            elif choice == "3":
                percent_main()
                break

            elif choice == "4":
                print("Exiting the application..")
                return
            
            else:
                print("Sorry! Please enter a valid choice.")

if __name__ == "__main__":
    main()

print("Thank you for using our application!")