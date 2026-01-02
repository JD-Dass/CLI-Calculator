import math

# SHOW MENU 
def show_menu():                 # create show menu function
    print("""        
          ========================================
          MY CALCULATOR : 
          ========================================
          0.  Exit
          1.  Addition
          2.  Subtraction
          3.  Multiplication
          4.  Divition
          5.  Power
          6.  Square Root
          7.  Modulus
          8.  Floor Value
          9.  Ceil Value
          10. Absolute Value
          11. Round Value
          ========================================
          """)                   # print my calculator menus using multiline command

# GET CHOICE
def get_choice():                # create get choice function
    while True:                  # while loop created , it's always tru , that means it's infinit loop
        try:                     # try and except , exception handler  
            choice = int(input("Select an option (0-11): "))    # the risky program entered. get the user valu and chenge str type into int 

            if choice in range(0, 12):                          #checked user entere the value between 0 and 4 using if statement                
                return choice                                   # if True then return the choice
            else:                                               # if fauls then print the following statement
                print("Invalid choice. Please select between 0 and 11.")
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
def divide(a, b):        # divition function into two numbers
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")   # raise zerodivition error for divided by zero is not allowed
    return a / b

#POWER
def power(a, b):           # power the programe
    return a ** b

#SQUARE ROOT
def square_root(a):        # square root program , not enter negative value
    if a < 0:              # if smaller then value user enter raise valueerror
        raise ValueError("Square root of negative number is not allowed")
    return math.sqrt(a)

#MODULUS
def modulus(a, b):         # modulus function
    return a % b

#FLOOR VALUE
def floor_value(a):        # floor function
    return math.floor(a)

#CEILING VALUE
def ceil_value(a):         # ceil function
    return math.ceil(a)

#ABSOLUTE VALUE
def absolute_value(a):     # absolute function
    return abs(a)

#ROUND VALUE
def round_value(a):        # round function
    return round(a)

# operations
operations = {   
    1: (add, 2),
    2: (subtract, 2),
    3: (multiply, 2),
    4: (divide, 2),
    5: (power, 2),
    6: (square_root, 1),
    7: (modulus, 2),
    8: (floor_value, 1),
    9: (ceil_value, 1),
    10: (absolute_value, 1),
    11: (round_value, 1)
}                         # create operations dictionary


#MAIN FUNCTION
def main():               # this is main function , connectinf all function
    while True:           # while loop uins infinit loop
        show_menu()       # show all menu
        choice = get_choice()                          #get choice from user

        if choice == 0:   # if user enter 0 calculator closed
            print("calculator closed. bye!")
            break                                      # if user enter zero exit the programe

        if choice not in operations:                   # if if user entered different numbers, through the following print 
            print("Invalid option selected")
            continue                                   # skip statement

        func, arg_count = operations[choice]           # assign the value for to func and arg count
        
        try:                                           # exception handling using try except
            if arg_count == 2:
                num1 = get_number("Enter first number: ")
                num2 = get_number("Enter second number: ")
                result = func(num1, num2)

            elif arg_count == 1:
                num = get_number("Enter number: ")
                result = func(num)

            print(f"Result: {result}")                 # print result
        
        except ZeroDivisionError as e:                 #handle the zero devition error
            print(f"Error: {e}")                       # print the error

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":                             # run only directly
    main()