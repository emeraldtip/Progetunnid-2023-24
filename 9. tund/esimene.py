sisend = input()
try:
    print(int(sisend) - 24)
except:
    # error juhtus sisendiks convertimisel, seega sisend pole arv
    if sisend.lower() == "programmeerimine":
        print("- on hea")
    elif len(sisend) > 10:
        print("See on pikk sõna")
    elif len(sisend) < 6:
        print("See on lühike sõna")
