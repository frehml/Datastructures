class Queue:
    """
    creert een lege queue
    :param: self
    :return: Queue class
    :postconditie: je krijgt een Queue terug
    """
    def __init__(self):
        self.items = []
    
    """
    wist een queue
    :param: self
    :return: string
    :preconditie: self bestaat
    :postconditie: self bestaat niet meer
    """
    
    """
    bepaalt of een queue leeg is
    :param: self
    :return: bool
    """
    def isEmpty(self):
        return len(self.items) == 0
    
    """
    voegt een element toe aan de queue
    :param: self, ele
    :return: void
    :postconditie: er zit een element meer in de queue
    """
    def enqueue(self, el):
        self.items.insert(0, el)
    
    """
    verwijdert het eerste element dat in de queue is toegevoegd
    :param: self
    :return: void
    :postconditie: er zit een element minder in de queue
    """
    def dequeue(self):
        self.items.pop()

    """
    vraagt het eerste toegevoegde element in de queue op
    :param: self
    :return: het eerste element in de queue
    """
    def getFront(self):
        return self.items[-1]