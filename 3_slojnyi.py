f = open('17_test.txt')
s = [int(x) for x in f]
kol = 0
maxi = 0
for x in range(len(s) - 2):
    tek = s[x] + s[x + 1] + s[x + 2]
    if str(tek) == str(tek)[::-1]:
        if (len(str(s[x])) == len(set(str(s[x])))) + (len(str(s[x + 1])) == len(set(str(s[x + 1])))) + (
                len(str(s[x + 2])) == len(set(str(s[x + 2])))) == 3:
            kol += 1
            if tek > maxi:
                maxi = tek

print(kol, maxi)
