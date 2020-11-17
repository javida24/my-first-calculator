print("Welocme to Javid's calculator")
print('Please input a number')
a = int(input())
print('For Sum enter: +')
print('For Minus enter: -')
print('For Multiplied enter: *')
print('For Divide enter: /')
print('For Power enter: ^')
act = input()
print('Please input second number')
b = int(input())
if act == '+':
    print(a+b)
elif act == '-':
    print(a-b)
elif act == '*':
    print(a*b)
elif act == '/':
    print(a/b)
elif act == '^':
    print(a**b)
else:
    print("you're enter wrong number or method, Please try again")

        
