a = float(input("Sisesta esimene arv: "))
mark = input("Sisesta tehtemärk (+|-|*|/): ")
b = float(input("Sisesta teine arv: "))

if mark == "+":
    print(a+b)
elif mark == "-": 
    print(a-b)
elif mark == "*": 
    print(a*b)
elif mark == "/": 
    print(a/b)