#Simple user input calculator

#1st step is to ask the user the numbers for calculation
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))

#Asking the user to choose an operation
operation=input(("Choose an operation (+, -, *, /): "))

if operation=="+":
    result= num1+num2
    print("The result is:", result)
    
elif operation=="-":
    result=num1-num2
    print("The result is:", result)
    
elif operation=="*":
	result=num1*num2
	print("The result is:", result)

elif operation=="/":
	if num2!=0:
	    result=num1/num2
	    print("The result is:", result)
	else:
		print("Error, cannot divide by zero")
	
else:
	print("This is an invalid operator sign")