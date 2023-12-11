# formReadDierenGui.py
# Anjo Eijeriks
# 2023/12/11 v2

import tkinter as tk                            # nodig voor de GUI
from Dier import Dier                           # omdat we oop doen

# methode voor de sluiten-knop
def sluiten():
    venster1.destroy()

# Het formulier 
venster1 = tk.Tk()
venster1.title("formReadDieren.py")
kop_label = tk.Label(text="Afdrukken alle dieren",
                     padx=10,                   # beetje ruimte links en rechts van kop_label
                     bg="white", fg="green",    # background en foreground
                     relief = tk.RIDGE          # mooi randje om kop_label)
)
kop_label.config(font=("Courier", 20))          #lettertype en grootte
kop_label.grid()

tekstvak = tk.Text(venster1,            # Tekstvak voor de resultaten
              height=40, width=60)
tekstvak.grid()             

mededeling_label = tk.Label(text="Dit zijn alle gevonden dieren.") 
mededeling_label.grid()

sluiten_knop = tk.Button(text="Sluiten",        # sluitenknop
                         command=sluiten)
sluiten_knop.grid()

# het eigenlijke programma
# properties zijn niet belangrijk, we willen alle dieren zien
dierid = None
soort = None
naam = None

nieuw_dier = Dier(dierid, soort, naam)          # maak een object aan
# het object leest alle dieren in de tabel uit en stopt ze in de array 'dieren'
dieren = nieuw_dier.read_dieren(dierid, soort, naam) 
for dier in dieren:                             # uitlezen van de array 'dieren'
    tekstvak.insert(tk.END, f"Dier ID: {dier[0]}, Soort: {dier[1]}, Naam: {dier[2]}\n")

venster1.mainloop()                             # lus blijft wachten op invoer
