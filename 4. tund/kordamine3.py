küsimine = True
asjad = []
while küsimine:
    sis = input("Sisesta sõna: ")
    if sis == "STOP":
        küsimine = False
    else:
        asjad.append(sis)



sonastik = {}
for i in asjad:
    if i in sonastik.keys(): 
        sonastik[i]+=1 #esineb teist või rohkemat korda, suurendame hulga väärtust 1 võrra
    else:
        sonastik[i]=1 #esineb esimest korda, seega paneme väärtuseks 1
print(sonastik)



#Või alternatiivselt (parem lahendus - kiirem ja vähem koodi vaja kirjutada)
sonastik = {}
for i in asjad:
    sonastik[i] = sonastik.get(i,0)+1 #vaata 3. tunni esitlust - mida teeb dictionary.get() funktsioon?
print(sonastik)