arvud = [167,38829017,12938712,23,4323,52,3,234,234]
korrutatud = {}
for arv in arvud:
    arv = str(arv)
    sum=int(arv[0])
    for e in arv[1:]:
        sum*=int(e)
    korrutatud[int(arv)]=sum

print(sorted(arvud, key=lambda num: (korrutatud[num]))) #lambda sort jälle 