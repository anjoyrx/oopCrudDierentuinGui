# formSearchDier.py
# Anjo Eijeriks
# 2023/11/30 v1

from Dier import Dier               # omdat we OOP doen
print("Opzoeken dier")

dierid = input("Welk dierid zoek je? ")                
soort = None                        # soort en naam zijn niet nodig
naam = None

nieuw_dier = Dier(dierid, soort, naam)
print("Het object is aangemaakt")

# het gevonden dier komt in de array 'dieren'
dieren = nieuw_dier.search_dier(dierid, soort, naam)

for dier in dieren:
    print(f"Dier ID: {dier[0]}, Soort: {dier[1]}, Naam: {dier[2]}")
