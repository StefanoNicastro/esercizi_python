#Dati dei corsi organizzati in diverse citta
corsi = (
    ("Milano", [
        ("gennaio", ("online", 50)),
        ("gennaio", ("in presenza", 30)),
        ("febbraio", ("online", 40)),
        ("febbraio", ("in presenza", 25)),
        ("marzo", ("online", 55)),
        ("marzo", ("in presenza", 65))
    ]),
    ("Bologna", [
        ("gennaio", ("online", 45)),
        ("gennaio", ("in presenza", 20)),
        ("febbraio", ("online", 35)),
        ("febbraio", ("in presenza", 30)),
        ("marzo", ("online", 75)),
        ("marzo", ("online", 5))
    ]),
    ("Bari", [
        ("gennaio", ("in presenza", 5)),
        ("gennaio", ("in presenza", 10)),
        ("febbraio", ("online", 23)),
        ("febbraio", ("in presenza", 2)),
        ("marzo", ("in presenza", 15)),
        ("marzo", ("in presenza", 52))
    ]),
    ("Catania", [
        ("gennaio", ("online", 53)),
        ("gennaio", ("in presenza", 12)),
        ("febbraio", ("in presenza", 27)),
        ("febbraio", ("online", 20)),
        ("marzo", ("online", 15)),
        ("marzo", ("in presenza", 52))
    ])
)

def analizza_partecipanti(città, modalità):
    mediaPart=0
    maxPart=0
    meseMaxPart=0
    cont=0

    conferma=False

    for luogo, dati in corsi:
        if luogo==città:
            conferma=True
            for mese, (mod, partecipanti) in dati:
                if cont==0 and mod==modalità:
                    maxPart=partecipanti
                    meseMaxPart=mese
                else:
                    if mod==modalità and partecipanti>maxPart:
                        maxPart=partecipanti
                        meseMaxPart=mese

                if mod==modalità:
                    mediaPart+=partecipanti
                    cont+=1
    if conferma==False:
        print("Città inserita non presente")


    mediaPart/=cont
    return (mediaPart, (maxPart, meseMaxPart))



while True:
    città=input("Inserisci il nome della città ")

    while True:
        modalità=input("Inserisci la modalità ")
        if modalità=="in presenza" or modalità=="online":
            break
        else:
            print("Modalità non valida, reinserire")

    print(analizza_partecipanti(città, modalità))