chislo = int(input())
fibonachi = [1]
num1 = 0
num2 = 1
while len(fibonachi) < chislo:
    num3 = num2 + num1 
    fibonachi.append(num3)
    num1 = num2
    num2 = num3
print(fibonachi)


