a = 0
vale = True
while vale:
	try:
		a = float(input("Sisesta esimene arv: "))
		vale = False
	except:
		print("Sisestatud arv pole õiges formaadis")
		vale = True



mark = input("Sisesta tehtemärk (+|-|*|/): ")


b = 0
vale = True
while vale:
	try:
		b = float(input("Sisesta teine arv: "))
		vale = False
	except:
		print("Sisestatud arv pole õiges formaadis")
		vale = True


if mark == "+":
    print(a+b)
elif mark == "-": 
    print(a-b)
elif mark == "*": 
    print(a*b)
elif mark == "/": 
    print(a/b)