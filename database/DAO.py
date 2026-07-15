from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente

class DAO():

    @staticmethod
    def getCorsiPD(pd):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT* FROM CORSO WHERE pd=%s  "
        cursor.execute(query, (pd,))
        res = []

        for row in cursor:
            res.append(Corso(**row)) #mi riempie  la lista di oggetti di tipo Corso con i valori di Corso

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCorsiPDwIscritti(pd):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT c.codins, c.crediti, c.nome, c.pd, COUNT(*) AS n
                   FROM corso c, iscrizione i
                   WHERE c.codins = i.codins AND c.pd = %s
                   GROUP BY c.codins, c.crediti, c.nome, c.pd"""
        cursor.execute(query, (pd,))
        res = []

        for row in cursor:
            res.append((Corso(codins=row["codins"],
                              crediti=row["crediti"],
                              nome=row["nome"],
                              pd=row["pd"]),
                        row["n"]))
        cursor.close()
        cnx.close()
        return res


    @staticmethod
    def getAllCorsi():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM corso"""
        cursor.execute(query)  # ← nota: niente secondo argomento!
        res = []
        for row in cursor:
            res.append(Corso(**row)) #Corso(**row),
            # perché la riga ha esattamente
            # i quattro campi del Corso (nessun n di troppo).
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getStudentiCorso(codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT s.*
                   FROM studente s, iscrizione i
                   WHERE s.matricola = i.matricola AND i.codins = %s"""

        cursor.execute(query, (codins,))

        res = []
        for row in cursor:
            res.append(Studente(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCDSofCorso(codins):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """SELECT s.CDS, COUNT(*) AS n
                   FROM studente s, iscrizione i
                   WHERE s.matricola = i.matricola
                     AND i.codins = %s
                     AND s.CDS != ""
                   GROUP BY s.CDS"""

        cursor.execute(query, (codins,))

        res = []
        for row in cursor:
            res.append((row["CDS"], row["n"]))

        cursor.close()
        cnx.close()
        return res