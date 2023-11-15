print("Sisesta 5 sõna")
sõnad = []
for i in range(5):
    # sisendit ei pea muutujasse toppima vaid võib ka otse listi lisada:
    sõnad.append(input("Sisesta sõna nr", i + 1))  # i+1, kuna python alustab lugemist 0-st
    
