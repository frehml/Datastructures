# map (dictionary) voor reservatie
# dictionary met als key: id en als value userid, timestamp, vertoning, plaatsen
# {id => [userid, timestamp, vertoning, plaatsen]}

"""reservaties = {1: [1, "2018-12-25 09:27:53", vertoning_instance, 3]
               2: [2, "2018-12-23 09:27:53", vertoning_instance, 5]}"""

class Reservatie:
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


    def is_empty(reservaties):
        """"Bepaalt of een map leeg is, de voorstelling kan begginnen if true
        Args:
            reservaties

        Returns:
            bool true or false"""
        pass


    def get_length(reservaties):
        """"Geeft de lengte van reservaties
        Args:
            reservaties

        Returns:
            int (>= 0)
        """


    def insert(id, lijst):
        """"Voegt een reservatie toe aan reservaties
        Args:
            id (hash, int>0)
            lijst ([userid, timestamp, vertoning, plaatsen])

        Returns:
            reservaties met reservatie toegevoegd
        """
        pass


    def delete(id):
        """"verwijderd de reservatie uit reservaties (als de gast is aangekomen in kinepolis ==> vertoning starten if empty)
        Args:
            id (hash, int>0)

        Returns:
            reservaties met reservatie verwijderd"""
        pass


    def retrieve(id):
        """"Haalt reservate op met de unieke ID en geeft de lijst terug
        Args:
            id (hash, int>0)

        Returns:
            reservaties[id]:
            lijst ([userid, timestamp, vertoning, plaatsen])
        """
        pass
