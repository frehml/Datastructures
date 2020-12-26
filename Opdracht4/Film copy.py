# map (dictionary) voor film
# dictionary met als key: id en als value titel en rating
# {id => [titel, rating]}

""""films = {1: ["The Lion King", 5]
            2: ["Pirates of the Caribbean", 4]}"""

class Film:
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


    def is_empty(films):
        """"Bepaalt of films leeg is
        Args:
            films

        Returns:
            bool true or false"""
        pass


    def get_length(films):
        """"Geeft de lengte van films
        Args:
            films

        Returns:
            int (>= 0)
        """


    def insert(id, lijst):
        """"Voegt een film toe aan de map
        Args:
            id (hash, int>0)
            lijst ([titel, rating])

        Returns:
            films met film toegevoegd
        """
        pass


    def delete(id):
        """"verwijderd de film uit films
        Args:
            id (hash, int>0)

        Returns:
            films met film verwijderd"""
        pass


    def retrieve(id):
        """"Haalt film op met de unieke ID en geeft de lijst terug
        Args:
            id (hash, int>0)

        Returns:
            films[id]:
            lijst ([titel, rating])
        """
        pass
