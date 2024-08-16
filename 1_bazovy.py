f = open('17_test.txt')
s = [int(x) for x in f]
kol = 0
maxi = 0
srz = (s[1090] + s[1091] + s[1092]) / 3  # находим среднее арифметическое 1089, 1090 и 1091-го элементов

for x in range(len(s) - 1):
    sredtek = ((s[x] + s[x + 1]) / 2) # ср. арифметическое текущих 2-ух элементов
    if sredtek > srz:
        kol += 1
        if sredtek > maxi: # поиск максимального среднего арифметического
            maxi = sredtek
print(kol, maxi)
