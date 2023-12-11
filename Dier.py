# Dier.py
# Anjo Eijeriks
# 2023/11/30 V3

class Dier:
    # CONSTRUCTOR MET PROPERTIES ----------------------------------------------
    def __init__(self, dierid, soort, naam):
        self.__dierid = dierid  # Let op: we gebruiken dubbele 
        self.__soort = soort    # underscores om de attributen 
        self.__naam = naam      # privé te maken
        
        self.conn = None        # initialiseer connection variabele
        self.cursor = None      # initialiseer cursor variabele
             
    # DATABASE METHODEN -------------------------------------------------------
    def open_database(self):
        import sqlite3
        self.conn = sqlite3.connect('dierentuin.db')
        self.cursor = self.conn.cursor()
        
    def sluit_database(self):
        self.conn.commit()
        self.conn.close()

    # CRUD METHODEN -----------------------------------------------------------
    # dier toevoegen aan de tabel dieren        
    def create_dier(self, dierid, soort, naam):
        self.__dierid = dierid
        self.__soort = soort
        self.__naam = naam

        self.open_database()
        insert_query = """
        INSERT INTO dieren(soort, naam) VALUES(?, ?)
        """
        self.cursor.execute(insert_query, (soort, naam))
        self.sluit_database()      

    # alle dieren van de tabel laten zien
    def read_dieren(self, dierid, soort, naam):
        self.open_database()
        select_query = """
        SELECT * FROM dieren
        """
        self.cursor.execute(select_query)
        dieren = self.cursor.fetchall()
        return dieren           # array 'dieren' gaat terug naar formReadDieren.py
        self.sluit_database()
            
    # dier in de tabel updaten
    def update_dier(self, dierid, soort, naam):   
        select_query = """
        UPDATE dieren
        SET soort = ?, naam = ?
        WHERE dierid = ? 
        """

        self.cursor.execute(select_query, (soort, naam, dierid))
        self.sluit_database()

    # dier uit de tabel verwijderen
    def delete_dier(self, dierid, soort, naam):
        self.__dierid = dierid
        self.open_database()
        select_query = """
        DELETE FROM dieren
        WHERE dierid = ?
        """
        self.cursor.execute(select_query, (dierid,))
        self.sluit_database()

    # dier in de tabel opzoeken
    def search_dier(self, dierid, soort, naam):
        self.__dierid = dierid
        self.open_database()

        select_query = """
        SELECT * FROM dieren
        WHERE dierid = ?
        """
   
        self.cursor.execute(select_query, (dierid,))
        dieren = self.cursor.fetchall()
        return dieren           # array met gevonden dier terug naar formSearchDier.py
        self.sluit_database()
    
    # SETTERS EN GETTERS ZIJN NIET NODIG --------------------------------------