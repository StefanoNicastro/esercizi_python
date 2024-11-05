dati=(("Milano", [("Gennaio", 18),("Febbraio", 10), ("Marzo","N/D")]),
("Monza",[("Gennaio", 4),("Febbraio","N/D"),("Marzo", 6)]),
("Arese",[("Gennaio", 1),("Febbraio",20),("Marzo", 11)]))

info=[]

def media(capoluogo,mesi):
    meseMin="no"
    meseMax="no"
    acqMin=0
    acqMax=0

    media=0
    cont=0
    for mese in mesi:
        if cont==0:
            acqMin=mese[1]
            acqMax=mese[1]
            meseMin=mese[0]
            meseMax=mese[0]
            if mese[1]=="N/D":
                acqMin=0
                acqMax=0
                meseMin=mese[0]
                meseMax=mese[0]

        if  mese[1]!="N/D" and mese[1]>acqMax:
            acqMax=mese[1]
            meseMax=mese[0]

        if mese[1]!="N/D" and mese[1]<acqMin:
            acqMin=mese[1]
            meseMin=mese[0]

        if mese[1]!="N/D":
            media=media+mese[1]
            cont+=1
    media/=cont
    info.append((capoluogo,(media,(meseMax,acqMax),(meseMin,acqMin))))

for cap in dati:
    mesi=cap[1]
    capoluogo=cap[0]
    media(capoluogo,mesi)

print(info)