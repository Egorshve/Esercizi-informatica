numero_nazioni=int(input("Quante nazioni vuoi inserire? "))
d={}
contatore=0
while True:
    nazione=input("Scrivi il nome della nazione: ")
    capitale=input("Scrivi il nome della capitale: ")
    d[nazione]=capitale
    contatore+=1
    if contatore==numero_nazioni:
        break

richiesta=input("Scrivi il nome del paese del quale vuoi sapere la capitale: ")
if richiesta in d:
    print(d[richiesta])
else:
    print("Questo paese non è presente")