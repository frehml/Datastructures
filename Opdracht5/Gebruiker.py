import LinkedList
# map (dictionary) voor gebruiker
# dictionary met als key: id en als value voornaam, achternaam en email
# {id => [voornaam, achternaam, email]}

"""gebruikers = {1: ['Bert', 'Feltch', 'Bert.Feltch@student.uantwerpen.be'],
              2: ['Robert', 'Bellen', 'Robert@gmail.com']}"""

class Gebruiker:
    def __init__(self):
        self.gebruikers = LinkedList()

    def create_user():
        pass

    def create():
        """"creert een map
        Args:

        Returns:
            Empty map"""
        pass


    def destroy():
        """"verwijderd een map
        Args:

        Returns:
                void (removes map)"""
        pass


    def is_empty(gebruikers):
        """"Bepaalt of gebruikers leeg is
        Args:
            gebruikers

        Returns:
            bool true or false"""
        pass


    def get_length(gebruikers):
        """"Geeft de lengte van gebruikers
        Args:
            gebruikers

        Returns:
            int (>= 0)
        """


    def insert(id, lijst):
        """"Voegt een gebruiker toe aan gebruikers
        Args:
            id (hash, int>0)
            lijst ([voornaam, achternaam, email])

        Returns:
            gebruikers met gebruiker toegevoegd
        """
        pass


    def delete(id):
        """"verwijderd de gebruiker uit gebruikers
        Args:
            id (hash, int>0)

        Returns:
            gebruikers met gebruiker verwijderd"""
        pass


    def retrieve(id):
        """"Haalt gebruiker op met de unieke ID en geeft de lijst terug
        Args:
            id (hash, int>0)

        Returns:
            gebruikers[id]:
            lijst ([voornaam, achternaam, email])
        """
        pass
