action = input()
num1 = input()
num2 = input()

print(type(num1))
print(type(num2))
if action == '+':
    print(int(num1) + int(num2))
elif action == '-':
    print(num1 - num2)
elif action == '*':
    print(num1 * num2)
elif action == '/':
    print(num1 / num2)
else:
    print('error')
