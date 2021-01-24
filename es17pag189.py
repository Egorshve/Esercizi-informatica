numero_capitali=int(input("Quante capitali vuoi inserire? "))
d={}
contatore=0
while True:
    capitale=input("Scrivi il nome della capitale: ")
    nazione=input("Scrivi il nome della nazione: ")
    d[capitale]=nazione
    contatore+=1
    if contatore==numero_capitali:
        break

richiesta=input("Scrivi il nome della capitale della quale vuoi sapere la nazione: ")
if richiesta in d:
    print(d[richiesta])
else:
    print("Questo paese non è presente")