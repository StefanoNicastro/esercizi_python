tupla_partite = (
    ("GiocatoreA", "GiocatoreB", 3, 2),
    ("GiocatoreC", "GiocatoreD", 2, 3),
    ("GiocatoreB", "GiocatoreC", 3, 0),
    ("GiocatoreA", "GiocatoreD", 3, 1),
    ("GiocatoreB", "GiocatoreD", 2, 3),
)

"""
media_set_partita(tupla_partite): Una funzione che accetti come parametro la tupla delle partite e restituisca la media dei set giocati per partita (somma dei set vinti da entrambi i giocatori divisa per il numero totale di partite).

media_set_giocatore(tupla_partite, giocatore): Una funzione che accetti come parametri la tupla delle partite e il nome di un giocatore, e restituisca la media dei set vinti dal giocatore in tutte le partite disputate.

match_piu_combattuto(tupla_partite): Una funzione che restituisca una tupla contenente il match con il maggior numero di set complessivi giocati e i relativi punteggi.

match_meno_combattuto(tupla_partite): Una funzione che restituisca una tupla contenente il match con il minor numero di set complessivi giocati e i relativi punteggi.

percentuale_vittorie_giocatore(tupla_partite, giocatore): Una funzione che restituisca la percentuale di partite vinte dal giocatore rispetto al totale delle partite disputate.

Prevedi un menu di scelta che consenta all'utente di selezionare un'operazione tra le opzioni disponibili.
"""

def media_set_partita(tupla_partite):
    cont=0
    media=0
    for giocatore1, giocatore2, vinti1, vinti2 in tupla_partite:
        media+=vinti1+vinti2
        cont+=1
    media/=cont
    print(f"Partite giocate: {cont}\nMedia set a partita: {media}")



def media_set_giocatore(tupla_partite, giocatore):
    cont=0
    media=0
    for giocatore1, giocatore2, vinti1, vinti2 in tupla_partite:
        if giocatore==giocatore1:
            media+=vinti1
            cont+=1
        elif giocatore==giocatore2:
            media+=vinti2
            cont+=1
    media/=cont
    print(f"{giocatore} ha giocato {cont} partite\ncon un media di {media} set vinti a partita")



def match_piu_combattuto(tupla_partite):
    partita=[]
    partite=[]

    cont=0
    for giocatore1, giocatore2, vinti1, vinti2 in tupla_partite:
        if cont==0:
            partita=[giocatore1, giocatore2, vinti1, vinti2]
        elif (partita[2]+partita[3])<(vinti1+vinti2) and cont!=0:
            partita=[giocatore1, giocatore2, vinti1, vinti2]

    setG=partita[2]+partita[3]
    partite.append(partita)

    for giocatore1, giocatore2, vinti1, vinti2 in tupla_partite:
        if vinti1+vinti2==setG and ((giocatore1 and giocatore2) != (partita[0] and partita[1])):
            partita=[giocatore1, giocatore2, vinti1, vinti2]
            partite.append(partita)

    return tuple(partite)



def match_meno_combattuto(tupla_partite):
    sommaRis=[]
    partite=[]

    cont=0
    for giocatore1, giocatore2, vinti1, vinti2 in tupla_partite:
        sommaRis.append(vinti1+vinti2)
    
    risMin=min(sommaRis)
    for giocatore1, giocatore2, vinti1, vinti2 in tupla_partite:
        if vinti1+vinti2==risMin:
            partite.append(tupla_partite[cont])
            cont+=1
        else:
            cont+=1

    return tuple(partite)



def percentuale_vittorie_giocatore(tupla_partite, giocatore):
    cont=0
    partVinte=0
    for giocatore1, giocatore2, vinti1, vinti2 in tupla_partite:
        if giocatore==giocatore1:
            if vinti1>vinti2:
                partVinte+=1
                cont+=1
            else:
                cont+=1
        
        elif giocatore==giocatore2:
            if vinti2>vinti1:
                partVinte+=1
                cont+=1
            else:
                cont+=1
    percVinte=100*partVinte/cont
    print(f"{giocatore} ha una percentuale di vittoria del {percVinte}%")



while True:
    print("0.Esci\n1.Media set a partita\n2.Media set vinti per giocatore specifico\n3.Match con più set\n4.Match con meno set\n5.Percentuale vittoria giocatore specifico")

    scelta=int(input("Inserisci l'opzione scelta "))
    while scelta<0 or scelta>5:
        scelta=int(input("Scelta non valida, reinserire "))
    
    if scelta==0:
        break

    elif scelta==1:
        media_set_partita(tupla_partite)

    elif scelta==2:
        pres=False
        giocatore=input("Inserisci il nome del giocatore ")
        
        for giocatore1, giocatore2, vinti1, vinti2 in tupla_partite:
            if giocatore==giocatore1 or giocatore==giocatore2:
                pres=True
        
        if pres==True:
            media_set_giocatore(tupla_partite, giocatore)
        else:
            print("Giocatore non presente")

    elif scelta==3:
        print(f"Match più giocato: {match_piu_combattuto(tupla_partite)}")
    
    elif scelta==4:
        print(f"Match meno giocato: {match_meno_combattuto(tupla_partite)}")
        #!CORREGGILO
    
    elif scelta==5:
        giocatore=input("Inserisci il nome del giocatore ")
        percentuale_vittorie_giocatore(tupla_partite, giocatore)

print("Programma interrotto")