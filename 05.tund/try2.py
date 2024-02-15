a = 0
vale = True
while vale:
    try:
        a = float(input("Sisesta üks arv (mitte null): "))
        print("Kahe jagamine selle arvuga annaks tulemuse:", 2 / a)
        vale = False
    except:
        print("Ma ütlesin, et sisesta ARV, mis pole NULL")
        vale = True
