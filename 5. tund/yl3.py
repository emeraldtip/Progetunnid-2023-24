jooksmas = True
nimekiri = []
while jooksmas:
	a = input()
	if a == "STOP":
		jooksmas = False
	else:	
		nimekiri.append(a)

print(sorted(nimekiri, key=len))