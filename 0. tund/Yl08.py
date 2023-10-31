sone = input()
tahed = []
for taht in sone:
    if (taht.isnumeric()):
        if int(taht)<5:
            tahed.append(taht)
    else:
        tahed.append(taht)
        
print(tahed)