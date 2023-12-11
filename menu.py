# menu.py
# Anjo Eijeriks
# 2023/12/09 V2

import tkinter as tk
import os

# De bij de menukeuzen behorende methoden
def afsluiten():
    root.destroy()

def open_formCreateDier():
    os.system("python formCreateDier.py")

def open_formReadDieren():
    os.system("python formReadDieren.py")

def open_formUpdateDier():
    os.system("python formUpdateDier.py")

def open_formDeleteDier():
    os.system("python formDeleteDier.py")
root = tk.Tk()

def open_formSearchDier():
    os.system("python formSearchDier.py")

# Het formulier zelf
root.title("Dierentuin menu")

# Maak een menubalk
menubalk = tk.Menu(root)

# Maak een menu "Bestand" en voeg het toe aan de menubalk
bestand_menu = tk.Menu(menubalk, tearoff=0)
bestand_menu.add_command(label="Afsluiten", command=afsluiten)
menubalk.add_cascade(label="Bestand", menu=bestand_menu)

# Maak een menu "Beheer dieren" en voeg het toe aan de menubalk
dier_menu = tk.Menu(menubalk, tearoff=0)
dier_menu.add_command(label="Create dier", command=open_formCreateDier)
dier_menu.add_command(label="Read dieren", command=open_formReadDieren)
dier_menu.add_command(label="Update dier", command=open_formUpdateDier)
dier_menu.add_command(label="Delete dier", command=open_formDeleteDier)
dier_menu.add_command(label="Search dier", command=open_formSearchDier)
menubalk.add_cascade(label="Dieren", menu=dier_menu)

# Toon het menu
root.config(menu=menubalk)

# Toon het hoofdvenster
plaatje=tk.PhotoImage(file='zooKlein.png')      # plaatje laden
labelPlaatje = tk.Label(image=plaatje)          # label voor het plaatje
labelPlaatje.grid()                             # label zichtbaar maken

root.mainloop()                                 # lus blijft wachten op invoer      
