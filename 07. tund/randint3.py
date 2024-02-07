from random import randint

jookseb = True
arv = randint(1, 100)

while jookseb:
    sisend = int(input("Arva ära üks arv 1-100: "))
    if sisend > arv:
        print("Sisend on suurem kui arv")
    elif sisend < arv:
        print("Sisend on väiksem kui arv")
    else:
        print("Palju õnne, arvasid arvu ära!")
        jookseb = False
