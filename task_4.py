import math
def geom_func(a, b, r, u, p=3.14):
    u1 = math.radians(u)
    St = 0.5* a * b * math.sin(u1)
    Sk = p*r**2
    Sp = a * b
    return St, Sk, Sp
figuri = geom_func(10, 20, 5, 30)
print(figuri)