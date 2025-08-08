# Simple User-input calculator with a repeat feature.

while True:
	
	# Ask user to input numbers
	num1 = float(input("Enter the first number: "))
	num2 = float(input("Enter the second number: "))
	
	# Ask user to choose an operation
	operation = input("Choose an operation (+, -, *, /, %, **): ")
	
	if operation == "+":
		result = num1 + num2
		print("The result is:", result)
		
	elif operation == "-":
		result = num1 - num2
		print("The result is:", result)
	
	elif operation == "*":
		result = num1 * num2
		print("The result is:", result)
	
	elif operation == "/":
		if num2 != 0:
			result = num1 / num2
			print("The result is:", result)
		else:
			print("Error: cannot divide by zero")
			
	elif operation == "%":
			result = num1 % num2
			print("The result is:", result)
			
	elif operation == "**":
			result = num1 ** num2
			print("The result is:", result)
			
	else:
		print("This is an invalid operator sign")
	
	# Ask user if they want to calculate again	
	again = input("Do you want to calculate again? (yes/no): ").lower()
	if again != "yes":
			print("Thank you for using the calculator. Goodbye!!!")
			break
