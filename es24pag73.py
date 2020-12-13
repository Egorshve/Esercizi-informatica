trump=0
biden=0
voti=0
while voti<10:
    voto=int(input("Chi voti?, TRUMP 1, BIDEN 2"))
    if voto==1:
        trump+=1
    if voto==2:
        biden+=1
    voti+=1
percentualetrump1=trump*100
percentualetrump=percentualetrump1/10
percentualebiden1=biden*100
percentualebiden=percentualebiden1/10
print("TRUMP",percentualetrump,"percentuale dei voti")
print("BIDEN",percentualebiden,"percentuale dei voti")
if percentualetrump>percentualebiden:
    print("HA VINTO TRUMP")
if percentualebiden>percentualetrump:
    print("HA VINTO BIDEN")
else:
    print("PARITA'")