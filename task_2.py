n = int(input('кол-во членов прогрессии'))
g = 0
num1 = int(input("первый член прогрессии"))
znam = int(input('знаменатель'))
while g < n:
    print(num1)
    num1 *= znam
    g += 1