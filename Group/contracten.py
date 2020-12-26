class film:
    def __init__(self, id = -1, title = "", beoordeling = -1.0):
        """
        __init__:   maakt een nieuwe film aan

        ID:         Het identificatie nummer van de film
                    een strikt positief geheel getal

        titel:      De titel van de film
                    Een string

        rating:     De rating score die de film heeft behaald
                    een float groter of gelijk aan nul en kleiner of gelijk aan 1

        Zoeksleutel:De sleutel waarmee die element kan worden gezocht
                    een strikt positief geheel getal

        precondities:   geen

        postcondities:  een bestaande film
        """

class gebruiker:
    def __init__(self, id=-1, vnaam="", anaam="", email=""):
        """
        __init__:       maakt een nieuwe reservatie aan

        ID:             het identificatie nummer van de gebruiker
                        strikt positief geheel getal

        voornaam:       De voornaam van de gebruiker
                        een string waarvan de eerste letter upper case is en de rest lower case

        achternaam:     De achternaam van de gebruiker
                        een string waarvan de eerste letter upper case is en de rest lower case

        emailadres:    het e-mailadres van de gebruiker
                        een string

        Zoeksleutel:    De sleutel waarmee die element kan worden gezocht
                        een strikt positief geheel getal

        precondities:   geen

        postcondities:  een bestaande gebruiker
        """

class Zaal:
    def __init__(self, zaalNummer = -1, aantalPlaatsen = -1):
        """
        __init__:       maakt een nieuwe zaal aan

        zaalNummer:     het nummer waarop de zaal zal worden gezocht
                        strikt positief geheel getal

        aantalPlaatsen: het totaal aantal plaatsen in de zaal
                        strikt positief geheel getal

        precondities:   geen

        postcondities:  een bestaande zaal
        """

class vertoning:
    def __init__(self, id = -1, zaalNummer = -1, slot = 0.0, date = (0,0,0), filmid = -1, vrijPlaats =-1):
        """
        __init__:   maakt een nieuwe vertoning aan

        id:         Het identificatienummer van de vertoning
                    een strikt positief getal

        zaalNummer: Het nummer van de zaal waarin de vertoning zal gebeuren
                    een strikt positief getal

        slot:       Het tijdsslot waarin de vertoning gebeurd
                    tuple van floating point getallen die groter zijn dan 0 en kleiner dan 24

        datum:      de datum waarop de vertoning speelt
                    een triplet van gehele getallen in de orde (dag, maand, jaar)
                    dag en maand zijn strikt positief en niet nul

        filmID:     Het id van de film die wordt vertoond
                    een strikt positief geheel getal

        vrijPlaats: Het aantal vrije plaatsen van de vertoning
                    een strikt positief geheel getal

        Zoeksleutel:De sleutel waarmee die element kan worden gezocht
                    een strikt positief geheel getal

        precondities:   geen

        postcondities:  een bestaande vertoning
        """