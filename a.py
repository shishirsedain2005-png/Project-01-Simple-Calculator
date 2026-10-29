num1=float(input("Enter your first number->"))
num2=float(input("Enter your second number->"))

operation=input("Which mathematical operation do you want?(+, -, *, and /)")
if operation =="+":
    print(f'your {num1}{operation}{num2} is {num1+num2}')
elif operation =="-":
    print(f'your {num1}{operation}{num2} is {num1-num2}')
elif operation=="*":
    print(f'your {num1}{operation}{num2} is {num1*num2}')
elif operation=="/":
    print(f'your {num1}{operation}{num2} is {num1/num2}')
else:
    print("Wrong input:( . Watch the instructions clearly......")