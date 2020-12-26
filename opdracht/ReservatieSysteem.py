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
        self.gebruikers = LinkedList.LinkedList()
        self.films = LinkedList.LinkedList()
        self.vertoningen = Tree.BST(None)
        self.time = 0
        self.reservaties = Queue.Queue()
        self.zalen = {1: Zaal.Zaal(1, zaal1), 2: Zaal.Zaal(2, zaal2)}

    """
    maakt een gebruiker object en zet ze in de linkedlist van gebruikers
    :param: self, id, voornaam, achternaam, emailadress
    :return: gebruiker object
    """
    def maak_gebruiker(self, id, voornaam, achternaam, emailadress):
        gebruiker = Gebruiker.Gebruiker(id, voornaam, achternaam, emailadress)
        self.gebruikers.insert_end(LinkedList.ListNode(gebruiker))
        print('\n\nGebruiker succesvol toegevoegd!')
        print('lijst gebruikers:\n')
        self.toon_gebruikers()
        return gebruiker

    """
    print alle gebruikers in de linkedlist van gebruiekrs
    :param: self
    :return: string
    """
    def toon_gebruikers(self):
        print("id\tvoornaam\tachternaam\temail-adress")
        for user in self.gebruikers.display():
            print(str(user.id) + '\t' + user.voornaam + '      \t' + user.achternaam + '   \t' + user.emailadress)

    """
    maakt een film object en zet ze in de linkedlist van films
    :param: self, id, titel, rating
    :return: film objects
    """
    def maak_film(self, id, titel, rating):
        film = Film.Film(id, titel, rating)
        self.films.insert_end(LinkedList.ListNode(film))
        print('\n\nFilm succesvol toegevoegd!')
        print('lijst films:\n')
        self.toon_films()
        return film

    """
    print alle films in de linkedlist van films
    :param: self
    :return: string
    """
    def toon_films(self):
        print('id\ttitel\t\trating')
        for film in self.films.display():
            print(str(film.id) + '\t' + film.titel + '   \t' + str(film.rating))
    
    """
    maakt een vertoning object en zet ze in de BST van vertoningen
    :param: self, id, zaalnummer, slot, datum, filmid
    :return: vertoning object
    """
    def maak_vertoning(self, id, zaalnummer, slot, datum, filmid):
        vertoning = Vertoning.Vertoning(id, zaalnummer, slot, datum, filmid, self.zalen[zaalnummer].plaatsen)
        self.vertoningen.insert(id, vertoning)
        print("\n\nVertoning succesvol toegevoegd!")
        print('lijst vertoningen:\n')
        self.toon_vertoningen()
        return vertoning

    """
    print alle vertoningen in de BST van vertoningen
    :param: self
    :return: string
    """
    def toon_vertoningen(self):
        print("id\tzaalnr\tslot\tdatum\t\tfilmid\tvrije plaatsen")
        string = ""
        for vertoning in self.vertoningen.inorder():
            string = str(vertoning.value) + '\t' + str(vertoning.data.zaalnummer) + '\t' + str(vertoning.data.slot) + '\t' + str(vertoning.data.datum) + '\t' + str(vertoning.data.filmid) + '\t' + str(vertoning.data.vrijeplaatsen)
            print(string)
    
    """
    Verhoogt de tijd met X units
    :param: self, x
    :return: string
    """
    def increment_time(self, x):
        self.time += x
        time.sleep(x)
        print("\nDe tijd is " + str(x) +" units voorbij gegaan.")
        print("het is nu " + str(self.time) + " units.")

    """
    maakt een reservatie object en zet ze in de queue van reservaties
    :param: self, id, userid, timestamp, vertoningid, plaatsen
    :return: reservatie object
    """
    def maak_reservatie(self, id, userid, timestamp, vertoningid, plaatsen):
        reservatie = Reservatie.Reservatie(id,  userid, timestamp, vertoningid, plaatsen)
        self.reservaties.enqueue(reservatie)
        print('\n\nReservatie succesvol toegevoegd')
        print('lijst reservaties:\n')
        self.toon_reservaties()
        return reservatie

    """
    print alle reservaties in de queue van reservaties
    :param: self
    :return: string
    """
    def toon_reservaties(self):
        print("id" + "\t" + "userid" + "\t" + "timestamp" + "\t" +"vertoningid" + "\t" + "plaatsen")
        for item in self.reservaties.items:
            print(str(item.id) + '\t' + str(item.userid) + '\t' + str(item.timestamp) + '\t\t' + str(item.vertoningid) + '\t\t' + str(item.plaatsen))

    """
    verlaagt het aantal vrije plaatsen in een vertoningen adhv een reservatie
    :param: reservatie object
    :return: void
    """
    def verlaag_plaatsen(self, reservatie):
        vertoning = self.vertoningen.search(reservatie.vertoningid)
        vertoning.vrijeplaatsen = vertoning.vrijeplaatsen - reservatie.plaatsen
        self.printify(vertoning)
    
    """
    print de vrije plaatsen in een vertoning
    :param: vertoning
    :return: string
    """
    def printify(self, vertoning):
        print('\n\nHet aantal vrije plaatsen is: ' + str(vertoning.vrijeplaatsen))
        return vertoning

#opdrachten voor het systeem

systeem = ReservatieSysteem(70, 70)
tom = systeem.maak_gebruiker(1, 'Tom', 'Hofkens', 'tom.hofkens@gmail.com')
systeem.gebruikers.display()
els = systeem.maak_gebruiker(2, 'Els', 'Laenens', 'els.laenens@gmail.com')
matrix = systeem.maak_film(1, 'Matrix', 4)
vertoning2 = systeem.maak_vertoning(1, 1, "20:00", '11/12/2020', matrix.id)
inception = systeem.maak_film(2, 'Inception', 5)
vertoning1 = systeem.maak_vertoning(2, 2, '14:30', '09/12/2020', inception.id)
reservatie1 = systeem.maak_reservatie(1, tom.id, 0, matrix.id, 5)
reservatie2 = systeem.maak_reservatie(2, els.id, 1, inception.id, 2)
systeem.increment_time(2)
print('\n\n' "Eerste reservatie: "+ str(systeem.reservaties.getFront()))
systeem.verlaag_plaatsen(reservatie1)
systeem.reservaties.dequeue()
print('\n\nReservatie is succesvol verwijderd.\nlijst reservaties:')
systeem.toon_reservaties()
systeem.increment_time(1)
print('\n\n' "Tweede reservatie: "+ str(systeem.reservaties.getFront()))
systeem.verlaag_plaatsen(reservatie2)
systeem.increment_time(1)
print("\n\nInception speelt...")
systeem.increment_time(1)
print("\nInception is gedaan.")
vertoning1.vrijeplaatsen = systeem.zalen[vertoning1.zaalnummer].plaatsen
systeem.printify(vertoning1)
print("\n\nThe Matrix speelt...")
systeem.increment_time(1)
print("\nThe Matrix is gedaan.")
vertoning2.vrijeplaatsen = systeem.zalen[vertoning1.zaalnummer].plaatsen
systeem.printify(vertoning2)
print('\n')