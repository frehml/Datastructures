import LinkedList
import Gebruiker
import Film
import Tree
import Vertoning
import Queue
import Reservatie
import time
import Zaal

class ReservatieSysteem:
    """
    initializeerd object ReservatieSysteem
    :param: self, zaal1, zaal2
    :return: object reservatiesysteem
    """
    def __init__(self, zaal1, zaal2):
        pass

    """
    maakt een gebruiker object en zet ze in de linkedlist van gebruikers
    :param: self, id, voornaam, achternaam, emailadress
    :return: gebruiker object
    """
    def maak_gebruiker(self, id, voornaam, achternaam, emailadress):
        pass

    """
    print alle gebruikers in de linkedlist van gebruiekrs
    :param: self
    :return: string
    """
    def toon_gebruikers(self):
        pass

    """
    maakt een film object en zet ze in de linkedlist van films
    :param: self, id, titel, rating
    :return: film objects
    """
    def maak_film(self, id, titel, rating):
        pass

    """
    print alle films in de linkedlist van films
    :param: self
    :return: string
    """
    def toon_films(self):
        pass
    
    """
    maakt een vertoning object en zet ze in de BST van vertoningen
    :param: self, id, zaalnummer, slot, datum, filmid
    :return: vertoning object
    """
    def maak_vertoning(self, id, zaalnummer, slot, datum, filmid):
        pass

    """
    print alle vertoningen in de BST van vertoningen
    :param: self
    :return: string
    """
    def toon_vertoningen(self):
        pass
    
    """
    Verhoogt de tijd met X units
    :param: self, x
    :return: string
    """
    def increment_time(self, x):
        pass

    """
    maakt een reservatie object en zet ze in de queue van reservaties
    :param: self, id, userid, timestamp, vertoningid, plaatsen
    :return: reservatie object
    """
    def maak_reservatie(self, id, userid, timestamp, vertoningid, plaatsen):
        pass

    """
    print alle reservaties in de queue van reservaties
    :param: self
    :return: string
    """
    def toon_reservaties(self):
        pass

    """
    verlaagt het aantal vrije plaatsen in een vertoningen adhv een reservatie
    :param: reservatie object
    :return: void
    """
    def verlaag_plaatsen(self, reservatie):
        pass
    
    """
    print de vrije plaatsen in een vertoning
    :param: vertoning
    :return: string
    """
    def printify(self, vertoning):
        pass