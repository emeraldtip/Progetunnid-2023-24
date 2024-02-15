from random import randint

tahestik = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k","l","m","n","o","p","q","r","s","š","z","ž","t","u","v","w","õ","ä","ö","ü","x","y"]
sona = "" #tühi string
for i in range(10): #genereerime 10-tähelise sõna
    sona = sona + tahestik[randint(0, len(tahestik) - 1)] #liidame stringile juurde suvalise tähe

print(sona)
