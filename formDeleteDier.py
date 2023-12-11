# formDeleteDier.py
# Anjo Eijeriks
# 2023/11/30 v1

from Dier import Dier               # omdat we OOP doen
print("Verwijder dier")

dierid = input("Welk dierid wil je verwijderen? ")                
soort = None                        # soort en naam zijn niet nodig
naam = None

verwijder_dier = Dier(dierid, soort, naam)
print("Het object is aangemaakt")

# eerst gaan we het dier zoeken
# het gevonden dier komt in de array 'dieren'
dieren = verwijder_dier.search_dier(dierid, soort, naam)

for dier in dieren:
    print(f"Dier ID: {dier[0]}, Soort: {dier[1]}, Naam: {dier[2]}")
    dierid = dier[0]

antwoord = input("Wil je dit dier verwijderen? j/n ")

if antwoord == "j":
    # nu gaan we het verwijderen
    verwijder_dier.delete_dier(dierid, soort, naam)
    print("Het dier is verwijderd.")
else:
    print("Het dier is niet verwijderd")


