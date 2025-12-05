def znach(*a):
    b = 0
    for a1 in a:
        b += a1
    return b / len(a)
m = znach(2, 3, 5, 2)
print(m)