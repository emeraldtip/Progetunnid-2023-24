a = float(input("Sisesta esimene arv: ")) #kasutame float'i, et ka komakohtadega arve vastu võtta
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