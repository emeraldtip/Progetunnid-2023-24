jooksmas = True
nimekiri = []
while jooksmas:
	a = input()
	if a == "STOP":
		jooksmas = False
	else:	
		nimekiri.append(a)

for sõna in nimekiri:
	print(sõna[0])