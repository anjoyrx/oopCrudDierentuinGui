# formCreateDier.py
# Anjo Eijeriks
# 2023/12/09 v2

import tkinter as tk                            # nodig voor de GUI
from Dier import Dier                           # omdat we oop doen

# De bij de knoppen horende methoden
def sluiten():
    venster1.destroy()

def invoeren():
    dierid = None                               # niet nodig, tabel is autoincrement
    naam = naam_invoer.get()                    # haal de waarde uit het invoerveld
    soort = soort_invoer.get()

    nieuw_dier = Dier(dierid, soort, naam)      # maak een object aan
    nieuw_dier.create_dier(dierid, soort, naam) # het object zet zichzelf in de tabel

    mededeling_label.configure(
        text=f"Soort: {soort}, Naam: {naam} is in de tabel gezet."
    )

# Het formulier 
venster1 = tk.Tk()
venster1.title("formCreateDier.py")
kop_label = tk.Label(text="Invoeren nieuw dier",
                     padx=10,                   # beetje ruimte links en rechts van kop_label
                     bg="white", fg="green",    # background en foreground
                     relief = tk.RIDGE          # mooi randje om kop_label)
)
kop_label.config(font=("Courier", 20))          #lettertype en grootte
kop_label.grid()

soort_label = tk.Label(text="Wat voor soort? ") # invoeren soort
soort_label.grid()
soort_invoer = tk.Entry()
soort_invoer.grid() 

naam_label = tk.Label(text="Wat is de naam?")   # invoeren naam
naam_label.grid()
naam_invoer = tk.Entry()
naam_invoer.grid()

mededeling_label = tk.Label(text="")            # informeert over het aanmaken
mededeling_label.grid()

invoer_knop = tk.Button(text="Invoeren",        # invoerenknop
                        command=invoeren)
invoer_knop.grid()

sluiten_knop = tk.Button(text="Sluiten",        # sluitenknop
                         command=sluiten)
sluiten_knop.grid()

venster1.mainloop()                             # lus blijft wachten op invoer
