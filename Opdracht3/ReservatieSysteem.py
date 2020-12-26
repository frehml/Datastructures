"""
Zet nieuwe gebruiker in gebruikerslijst
:param: voornaam, achternaam, email
:return: bool (of het succesvol is)
"""
def maakAccount():
    pass


"""
zet reservatie in lijst reservaties
:param: userid, timestamp, vertoning, plaatsen
:return: bool (of het succesvol is)
"""
def maakReservatie():
    pass


"""
meldt de gebruiker aan
:param: gebruiker
:return: bool
"""
def meldAan():
    pass


"""
Ziet of account tussen gebruikers lijst staat en of gebruiker naar wachtwoord wijst
:param: account
:return: bool
"""
def isValidAccount():
    pass


"""
checkt of reservaties > zaal capaciteit
:param: vertoning
:return: bool
:preconditie: geeft een geldige vertoning
"""
def isUitverkocht():
    pass


"""
Wordt door isValidAccount geroepen als het geen valid account is en geeft een foutmelding terug
:param: void
:return: string
"""
def foutMelding():
    pass


""""
Geef alle films terug
:param: void
:return: list of movies
"""
def films():
    pass


"""
Haalt reservatie uit de lijst reservaties
:param: userid
:return: bool
:precondities: userid zit in de lijst reservaties
:postconditie: er zit 1 element minder in de lijst reservaties
"""
def annuleerReservatie():
    pass


"""
Logt de gebruiker uit het systeem
:param: userid
:return: bool of het gelukt is
:preconditie: geldige userid
"""
def logUit():
    pass

"""
Verwijdert de gebruiker uit de lijst van gebruikers
:param: userid
:return: bool
:preconditie: geldige userids
"""
def verwijderAccount():
    pass

"""
Lijst all uren van een film op
:param: titel
:return: data
:preconditie: geldige titel
"""
def urenFilm():
    pass


"""
Lijst alle vertoningen op
:param: void
:return: lijst vertoningen
"""
def vertoningen():
    pass
