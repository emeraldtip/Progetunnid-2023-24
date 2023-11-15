pikimpikkus = 0
pikimsõna = ""
for i in range(5):
    a = input("Sisesta üks sõna: ")
    if len(a) > pikimpikkus:
        pikimpikkus = len(a)
        pikimsõna = a

print("Pikim sõna on", pikimsõna, "ja selle pikkus on", pikimpikkus)
