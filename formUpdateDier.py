# formUpdateDier.py
# Anjo Eijeriks
# 2023/11/30 v1

from Dier import Dier               # omdat we OOP doen
print("Wijzigen dier")


dierid = input("Welk dierid zoek je? ")                
soort = None                        # soort en naam zijn niet nodig
naam = None

wijzig_dier = Dier(dierid, soort, naam)
print("Het object is aangemaakt")

# eerst gaan we het dier zoeken
# het gevonden dier komt in de array 'dieren'
dieren = wijzig_dier.search_dier(dierid, soort, naam)

for dier in dieren:
    dierid = dier[0]
    soort = dier[1]
    naam = dier[2]
    print("")
    print(f"Het dierid is: {dierid}")
    soort = input(f"De soort is: {soort}. Wat wordt de nieuwe soort? ")
    naam = input(f"De naam is: {naam}. Wat wordt de nieuwe naam? ")

# daarna gaan we het dier wijzigen
wijzig_dier.update_dier(dierid, soort, naam)

print("Deze gegevens staan nu in de tabel:")
print(f"{dierid}, {soort}, {naam}")

