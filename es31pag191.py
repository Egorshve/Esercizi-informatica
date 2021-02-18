dizionario={23:15000,27:28000,38:55000,41:75000,43:1000000}
reddito=int(input("Inserisci il reddito "))
if reddito<=dizionario[23]:
    imposta=reddito*23/100
    print("L'imposta è",imposta)
    tax_media=imposta/reddito*100
    print("La tassazione media è",tax_media)
if reddito<=dizionario[27] and reddito>=dizionario[23]:
    imposta=3450+reddito*27/100
    print("L'imposta è",imposta)
    tax_media=imposta/reddito*100
    print("La tassazione media è",tax_media)
if reddito<=dizionario[38] and reddito>=dizionario[27]:
    imposta=3450+3510+reddito*38/100
    print("L'imposta è",imposta)
    tax_media=imposta/reddito*100
    print("La tassazione media è",tax_media)  
if reddito<=dizionario[41] and reddito>=dizionario[38]:
    imposta=3450+3510+10260+reddito*41/100
    print("L'imposta è",imposta)
    tax_media=imposta/reddito*100
    print("La tassazione media è",tax_media)
if reddito<=dizionario[43] and reddito>=dizionario[41]:
    imposta=3450+3510+10260+8200+reddito*23/100
    print("L'imposta è",imposta)
    tax_media=imposta/reddito*100
    print("La tassazione media è",tax_media)