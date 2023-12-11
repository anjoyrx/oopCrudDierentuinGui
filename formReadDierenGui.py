# formReadDierenGui.py
# Anjo Eijeriks
# 2023/12/11 v2

import tkinter as tk                            # nodig voor de GUI
from Dier import Dier                           # omdat we oop doen

# De bij de knoppen horende methoden
def sluiten():
    venster1.destroy()


# properties zijn niet belangrijk, we willen alle dieren zien
dierid = None
soort = None
naam = None

nieuw_dier = Dier(dierid, soort, naam)      # maak een object aan
# het object leest alle dieren in de tabel uit en stopt ze in de array 'dieren'
dieren = nieuw_dier.read_dieren(dierid, soort, naam) 

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
              height=50, width=60)
tekstvak.grid()             

for dier in dieren:
    #print(f"Dier ID: {dier[0]}, Soort: {dier[1]}, Naam: {dier[2]}")
    tekstvak.insert(tk.END, f"Dier ID: {dier[0]}, Soort: {dier[1]}, Naam: {dier[2]}\n")

mededeling_label = tk.Label(text="Dit zijn alle gevonden dieren.")            # informeert over het aanmaken
mededeling_label.grid()

sluiten_knop = tk.Button(text="Sluiten",        # sluitenknop
                         command=sluiten)
sluiten_knop.grid()

venster1.mainloop()                             # lus blijft wachten op invoer
