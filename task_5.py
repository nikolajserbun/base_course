num1 = int(input())
num2 = int(input())
if num2 == 0:
    print('Нельзя делить на 0')
else:
    print(num1%num2, '-остаток', num1//num2, '-частное')