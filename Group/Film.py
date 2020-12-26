class Film:
    """
    Initialiseerd Film object
    :param: self, id, titel, rating
    :return: Film object
    """
    def __init__(self, id, titel, rating):
        pass

    """
    Verwijdert Film object instansie
    :param: film objects
    :return: string
    """
    def __del__(self):
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