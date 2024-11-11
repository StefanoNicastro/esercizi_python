dati_pluviometrici=(
    ("Milano", [("Gennaio", 10),("Febbraio", 9), ("Marzo", 7)]),
    ("Pavia", [("Gennaio", 5),("Febbraio", 8), ("Marzo", 12)]),
    ("Bergamo", [("Gennaio", 0),("Febbraio", 3), ("Marzo", 5)]),
    ("Brescia", [("Gennaio", 7),("Febbraio", 0), ("Marzo", 10)])
)

def mediaMaxMin(città, mesi_mm):

  media=0
  cont=0
  mmMin=0
  mmMax=0
  meseMin=0
  meseMax=0

  for dati in mesi_mm:
    for mese, mm in dati:
      if mm>0:
        media+=mm
        cont+=1
      
      if cont==1 and mm>0:
        mmMin=mm
        mmMax=mm
        meseMin=mese
        meseMax=mese
      elif cont>1 and mm>0:
        if mmMin>mm:
          mmMin=mm
          meseMin=mese
        if mmMax<mm:
          mmMax=mm
          meseMax=mese

  media/=cont
  stampa_tupla=(media,(mmMin,meseMin), (mmMax,meseMax))
  
  print(f"Città: {città}: {stampa_tupla}")

for (città, *mesi_mm) in dati_pluviometrici:
  mediaMaxMin(città, mesi_mm)
