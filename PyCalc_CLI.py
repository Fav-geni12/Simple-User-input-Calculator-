from math import sqrt

#Basic Calculator that calculates basic operation

#displaying a welcome message

print("Hi!!")
user_name = input("What's your name? ")
print("Welcome", user_name + "!","Enjoy your calculation.")


#asking for users input
while True:
    
    #enclosed the operation in try/except to handle errors
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        #asking users for operation type
        operations = ["+", "-", "*", "/", "**", "sqrt"]
        print("Operations", operations)
        operation = input("Enter operation: ")

        #start calculating
        if operation == "+":
            answer = num1 + num2
            print("Answer is: ", answer)

        elif operation == "-":
            answer = num1 - num2
            print("Answer is: ", answer)

        elif operation == "*":
            answer = num1 * num2
            print("Answer is: ", answer)

        elif operation == "/":
            if num2 == 0:
                print("Error: cannot divide by zero")
            else:
                answer = num1 / num2
                print("Answer is: ", answer)

        elif operation == "**":
            answer = num1 ** num2
            print("Answer is:", answer)

        elif operation == "sqrt":
            choice = input("Which number? Enter '1' for first number or Enter '2' for second number: ")
            if choice == "1":
                num = num1
            elif choice == "2":
                num = num2
            else:
                print("Invalid Choice")
                num = None

            if num is not None:
                if num <= 0:
                    print("Cannot take a square root of zero or a negative number")
                else:
                    answer = sqrt(num)
                    print("The square root of", num, "=", answer)

        else:
            print("Wrong operation input, please enter a valid operation from the operation list")
    except ValueError:
        print("Error: please enter valid numbers, not letters or symbols")

    #asks after the calculation is done
    entry = input("Type 'Done' when you're done calculating, or press Enter if you want to continue calculating: ")
    if entry.lower() == "done":
        print("Goodbye", user_name + "!", "Hope you enjoyed your calculation!")
        break
