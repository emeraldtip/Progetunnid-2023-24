sis = input("Sisesta midagi: ")
polesamataht = False


#peab ka intiks tegema kuna jagamise tulemus on float ja range funktsioonile see ei meeldi
for i in range(int(len(sis) / 2)): #peab ka intiks tegema kuna jagamise tulemus on float ja range funktsioonile see ei meeldi
    if sis[i] != sis[len(sis) - 1 - i]:
        polesamataht = True


if polesamataht:
    print("Ei ole palindroom")
else:
    print("On palindroom")
