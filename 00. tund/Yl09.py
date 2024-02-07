jookseb = True
sonad = []
while jookseb:
    s = input("sisesta sõna: ")
    if s == "STOP":
        jookseb = False
    else:
        sonad.append(s)

sonad = sorted(sonad, key=lambda sona: (len(sona),sona)) #lambadfunktsiooniga sortimine (soovitan uurida seda)

print("Lühim sõna: "+sonad[0])
print("Pikim sõna: "+sonad[-1])
print("Sorteeritud sõnad: "+str(sonad))