print("Sisesta 5 sõna")
sõnad = []
for i in range(5):
    # sisendit ei pea muutujasse toppima vaid võib ka otse listi lisada:
    print("Sisesta sõna nr", i + 1)
    sõnad.append(input())  # i+1, kuna python alustab lugemist 0-st

print()  # tühja rea jaoks
print("Nimekirjas esinevad sõnad:")
for sõna in sõnad:
    print(sõna)

print()  # tühja rea jaoks
print("Nimekirjas esineb sõna 'maja'", sõnad.count("maja"), "korda")

print()  # tühja rea jaoks
print("Nimekirjas esinevad sõnad, mis algavad a-tähega:")
for sõna in sõnad:
    if sõna[0] == "a" or sõna[0] == "A":
        print(sõna)
