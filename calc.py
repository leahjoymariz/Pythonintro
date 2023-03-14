# imports


# global vars


# functions

def print_menu():
    seperator = "-------------------"
    print(seperator)
    print(" Calc 3000")
    print(seperator)
    print("[1] Sum two numbers")
    print("[2] Subtract two numbers")
    print("[3] Multiply two numbers")


# plain instructions
print_menu()
opt = input("Please select an option: ")


if opt == "1":
    # ask the user for num1, num2 and print the results of adding those numbers
    num1 = float (input("Please provide num1: "))
    num2 = float (input("Please provide num2: "))
    result = num1 + num2
    print("The result is: " + str(result))

elif opt =="2":
    num2 = float (input("Please provide num2: "))
    num3 = float (input("Please provide num3: "))
    result = num2 - num3
    print("The result is: " + str(result))

elif opt =="3":
    num2 = float (input("Please provide num2: "))
    num3 = float (input("Please provide num3: "))
    result = num2 * num3
    print("The result is: " + str(result))


# division
# if the second numbe is zero, show an error
# else divide and show the result

elif opt =="4":
    
