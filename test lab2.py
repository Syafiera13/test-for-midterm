#
# Syafiera
# Calculator Lab 2
#

# Define Function
def cal(x1, x2, op):
    if op == '+':
        return int(x1) + int(x2)
    elif op == '-':
        return int(x1) - int(x2)
    elif op == '*':
        return int(x1) * int(x2)
    elif op == '/':
        return int(x1) / int(x2)

# 1. Input
x1 = input('Type x1: ')
x2 = input('Type x2: ')
op = input('Operator: ')

# 2. Process
sum = cal(x1, x2, op)

# 3. Output
print(f'Sum: {sum}')