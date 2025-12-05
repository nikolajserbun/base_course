def mec_eng(m, h, v, g = 9.8):
    pot_eng = m * g * h
    kin_eng = m * v**2 / 2
    return kin_eng + pot_eng
eng = mec_eng(2, 10, 5)
print(eng)