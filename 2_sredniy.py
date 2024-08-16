f = open('17_test.txt')
s = [int(x) for x in f]
kol = 0
maxi = 0
for x in range(len(s) - 2):
    if (s[x] + s[x + 1]) > s[x + 2]:
        if (s[x + 1] + s[x + 2]) > s[x]:
            if (s[x] + s[x + 2]) > s[x + 1]:
                kol += 1
                perimetr = s[x] + s[x + 1] + s[x + 2]
                if perimetr > maxi:
                    maxi = perimetr
print(kol, maxi)
