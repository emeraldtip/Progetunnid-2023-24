jookseb = True
arvud = []
while jookseb:
    s = input("Sisesta arv: ")
    if s == "STOP":
        jookseb = False
    else:
        arvud.append(int(s))
        
for i in sorted(arvud):
    print(i)
if len(arvud)>4:
    print("Viiendana sisestatud arv on",arvud[4])