import random

diz_chef={"Mario Rossi": [("Antipasto", (8,7,9), "Chef Junior"), ("Primi", (7,8,8),"Chef Junior"), ("Secondi",(9,9,8),"Chef Junior"), ("Dessert",(8,8,9),"Chef Junior")],
          "Luigi Bianchi": [("Antipasto", (7,7,8), "Chef Senior"), ("Primi", (8,9,7),"Chef Senior"), ("Secondi",(7,8,7),"Chef Senior"), ("Dessert",(9,8,8),"Chef Senior")],
          "Giulia Verdi": [("Antipasto", (9,8,8), "Chef Junior"), ("Primi", (8,7,9),"Chef Junior"), ("Secondi",(8,8,8),"Chef Junior"), ("Dessert",(7,9,8),"Chef Junior")],
          "Stefano Nicastro": [("Antipasto", (5,9,9), "Chef Senior"), ("Primi", (8,7,10),"Chef Senior"), ("Secondi",(8,8,7),"Chef Senior"), ("Dessert",(7,8,9),"Chef Senior")]}



def agg_piatti_unici():
    for chef in diz_chef.keys():

        n1=random.randint(1,10)
        n2=random.randint(1,10)
        n3=random.randint(1,10)
        votiNuovi=(n1,n2,n3) #

        categoria=""
        for tipoP, voti, categ in diz_chef[chef]:
            categoria=categ
            break
       
        diz_chef[chef].append(("Piatti speciali" , votiNuovi, categoria))



def mostra_chef():
    while True:
        chef=input("Inserisci il nome dello chef da cercare ")
        if chef not in diz_chef.keys():
            print("Nome non presente, reinserire")
        else:
            break
   
    print(f"Nome chef: {chef}")
    print(f"Categoria: {diz_chef[chef][0][2]}")
    for tipoP, voti, categ in diz_chef[chef]:
        print(f"Categoria piatto: {tipoP}")
        print(f"Creatività: {voti[0]}\nGusto: {voti[1]}\nPresentazione: {voti[2]}")
        print("")



def mostra_cat_piatto():

    tipi_piatto=[]
    for chef in diz_chef.keys():
        for tipoP, voti, categ in diz_chef[chef]:
            tipi_piatto.append(tipoP)

    while True:
        tipologia=input("Inserisci la categoria di piatti da stampare ")
        if tipologia not in tipi_piatto:
            print("Categoria non presente, reinserire")
        else:
            break
   
    for chef in diz_chef.keys():
        for tipoP, voti, categ in diz_chef[chef]:
            if tipoP==tipologia:
                print(f"Chef: {chef}\nCategoria: {categ}")
                print(f"Voti: creatività: {voti[0]}\nGusto: {voti[1]}\nPresentazione: {voti[2]}")
                print("")



def analisi_punteggioA(diz_chef, tipologia, categoria):
    somme_voti=[]
    nomi_chef=[]
   
    for chef in diz_chef.keys():
        for tipoP, voti, categ in diz_chef[chef]:
            if tipoP==tipologia and categoria==categ:
                nomi_chef.append(chef)
                somma=voti[0]+voti[1]+voti[2]
                somme_voti.append(somma)

    print(f"Chef con la somma di voti maggiore: {nomi_chef[somme_voti.index(max(somme_voti))]}\ncon una somma voti di: {max(somme_voti)}")



def analisi_punteggioB(diz_chef, tipologia, categoria):
    print(f"Tipologia piatto: {tipologia}\nCategoria chef: {categoria}")
    for chef in diz_chef.keys():
        for tipoP, voti, categ in diz_chef[chef]:
            if tipoP==tipologia and categoria==categ:
                media=float((voti[0]+voti[1]+voti[2])/3)
                print(f"Nome chef: {chef}\nMedia voti: {media}")
                print("")



def nuovo_chef(diz_chef, nominativo, risultati):
    risultati=inserisci_dati_nuovo_chef()

def inserisci_dati_nuovo_chef():
    risultati=[]

    while True:
        categ=input("Inserisi la categoria dello chef ")
        if categ!="Chef Senior" or categ!="Chef Junior":
            print("Categoria non valida, reinserire")
        else:
            break
   
    for i in range(5):
        if i==0:
            tipologia="Antipasto"
            print("Antipasto:")
        elif i==1:
            tipologia="Primi"
            print("Primi:")
        elif i==2:
            tipologia="Secondi"
            print("Secondi:")
        elif i==3:
            tipologia="Dessert"
            print("Dessert:")
        else:
            tipologia="Piatti speciali"
            print("Piatti speciali:")
        n1=int(input("Inserisci il voto in creatività "))
        n2=int(input("Inserisci il voto in gusto "))
        n3=int(input("Inserisci il voto in presentazione "))
        votiNuovi=[n1,n2,n3]
        risultati.append((tipologia, votiNuovi, categ))


     

agg_piatti_unici()


mostra_chef()


mostra_cat_piatto()



analisi_punteggioA(diz_chef, "Primi", "Chef Senior")

analisi_punteggioB(diz_chef, "Primi", "Chef Senior")
'''
nuovo_chef(diz_chef, ("Giulio", "Berardi"), [])
'''

'''
3. Usato una lista al posto della tupla, un for superfluo.
6. A/B Non ha eseguito il controllo dei parametri
7. Funzione non finita.

'''