asjad = ["Jehv","Jehv","Kaks","Tuhat","Seitseteist","Kaks","Üks","Kuus", "Auto"]
sonastik = {}
for i in asjad:
    if i in sonastik.keys():
        sonastik[i]+=1
    else:
        sonastik[i]=1
print(sonastik)



#Või alternatiivselt (parem lahendus)
sonastik = {}
for i in asjad:
    sonastik[i] = sonastik.get(i,0)+1
print(sonastik)