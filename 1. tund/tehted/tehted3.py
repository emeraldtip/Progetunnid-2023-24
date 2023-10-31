a = int(input("Sisesta esimene arv: "))
mark = input("Sisesta tehtemärk (+|-|*|/|**): ")
b = int(input("Sisesta teine arv: "))

if mark == "+":
    print(a+b)
elif mark == "-": 
    print(a-b)
elif mark == "*": 
    sum = 0
    for i in range(b):
        sum+=a
    print(sum)
elif mark == "/": #teeme jäägiga jagamist
    arv = 0
    while a>=b:
        a-=b
        arv+=1
    print(arv,"jääk",a)