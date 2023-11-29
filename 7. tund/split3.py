a = "1,4,5,6"
print(a)
b = a.split(",")
summa = 0
for x in b:
    summa = summa + int(x)
    print(summa)
print(summa)
