# SHOW MENU 
def show_menu():                 # create show menu function
    print("""        
          ========================================
          MY CALCULATOR : 
          ========================================
          1. Addition
          2. Subtraction
          3. Multiplication
          4. Divition
          0. Exit
          ========================================
          """)                   # print my calculator menus using multiline command

# GET CHOICE
def get_choice():                # create get choice function
    while True:                  # while loop created , it's always tru , that means it's infinit loop
        try:                     # try and except , exception handler  
            choice = int(input("Select an option (0-4): "))     # the risky program entered. get the user valu and chenge str type into int 

            if choice in [0, 1, 2, 3, 4]:                       #checked user entere the value between 0 and 4 using if statement                
                return choice                                   # if True then return the choice
            else:                                               # if fauls then print the following statement
                print("Invalid choice. Please select between 0 and 4.")
        except ValueError:                                      #if user entered not a number , except handled this, then print following statement
            print("Please enter a number only.")

# GET NUMBER
def get_number(prompt):           # get number function , the input sent parameter
    while True:                   # create infinit loop using while loop and it's lways True
        try:                      # create try except exception handling , the risk code inside try
            number = float(input(prompt))  # create number variyable , get user input and convert into float
            return number         # return the number and close function
        except ValueError:        # if user entered invalid input to handled the except valueerror and print following statement
            print("Invalid input. Please enter a valid number.")

#ADDITION FUNCTION
def add(a, b):             # addition function into two numbers
    return a + b

#SUBTRACTION
def subtract(a, b):        # subtraction function into two numbers
    return a - b

#MULTIPICATION
def multiply(a, b):        # multiplication function into two numbers
    return a * b

#DIVITION
def divition(a, b):        # divition function into two numbers
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")   # raise zerodivition error for divided by zero is not allowed
    return a / b

#MAIN FUNCTION
def main():               # this is main function , connectinf all function
    while True:           # while loop uins infinit loop
        show_menu()       # show all menu
        choice = get_choice()                          #get choice from user

        if choice == 0:
            print("calculator closed. bye!")
            break                                      # if user enter zero exit the programe

        num1 = get_number("Enter first numver: ")      # get first number from user
        num2 = get_number("Enter second number: ")     # get seconde number from user
        
        try:                                           # exception handling using try except
            if choice == 1:
                result = add(num1, num2)               # if user enter one then start addition

            elif choice == 2:
                result = subtract(num1, num2)          # if user enter two then start subtraction

            elif choice == 3:
                result = multiply(num1, num2)          # if user enter three then start multiplication
            elif choice == 4:
                result = divition(num1, num2)          # if user enter four then start divition

            print(f"Result: {result}")                 # print result
        
        except ZeroDivisionError as e:                 #handle the zero devition error
            print(f"Error: {e}")                       # print the error

if __name__ == "__main__":                             # run only directly
    main()