sonad = []
with open("yl10sisend.txt","r",encoding="UTF8") as file: #ei ole faili sulgemise ja avamise pärast vaja muretseda
    sonad = sorted([e for i in file.readlines() for e in i.split()]) #list comprehension

with open("yl10väljund.txt","w+",encoding="UTF8") as file: #w+ - teeb uue faili kui faili ei eksisteeri, muidu kirjutab sisu üle
    file.write(" ".join(sonad)+"\n")