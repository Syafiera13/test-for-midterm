#Syafiera
#Calculator

Sum = 0

#Input
while True:
    x1 = float(input("Enter First Number: "))
    x2 = int(input("ENter Second Number: "))
    Operator = (input("Enter what to do?: "))

#Process
    if Operator == "+":
        sum = float(x1) + int(x2)
    elif Operator == "-":
        sum = float(x1) - int(x2)
    elif Operator == "*":
        sum = float(x1) * int(x2)
    elif Operator == "/":
        sum = float(x1) / int(x2)

#Output
    print(f"Sum = {sum}")
    res = input("Continue? Yes/No: ")
    if res == "No":
        break;