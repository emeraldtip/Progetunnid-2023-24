jooksmas = True
hindeleht = {}
while jooksmas:
    nimi = input("Sisesta õpilase nimi: ")
    hinne = input("Sisesta õpilase hinne: ")
    hindeleht[nimi] = hinne
    jätk = input("Kas soovid jätkata? ")
    if jätk == "ei":
        jooksmas = False

eemaldatavad = []
for i in hindeleht: #käib läbi võtmed, sama mis hindeleht.keys()
    if hindeleht[i] == "2": #pole isegi vaja ümber muundada täisarvuliseks
        eemaldatavad.append(i) #me ei saa samal ajal asju, mida me üle käime muuta, seega paneme kirja, keda eemaldama peab ja eemaldame hiljem

for i in eemaldatavad:
     del(hindeleht[i])
     
print(hindeleht)