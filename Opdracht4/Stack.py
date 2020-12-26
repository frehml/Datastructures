class Stack:
    """
    creert een lege stack
    :param: self
    :return: Stack
    :postconditie: je krijgt een stack terug
    """
    def __init__(self):
        self.items = []

    """
    wist een stack
    :param: self
    :return: string
    :preconditie: self bestaat
    :postcondidite: self bestaat niet meer
    """
    def __del__(self):
        print("Delete sucessful")
    
    """
    bepaalt of een stack leeg is
    :param: self
    :return: bool
    """
    def isEmpty(self):
        return (len(self.items) == 0)
    
    """
    voegt een element toe aan de stack
    :param: self, el
    :return: void
    :postconditie: er zit een ele meer in de stack
    """
    def push(self, el):
        self.items.append(el)
    
    """
    verwijdert het laatst toegevoegde element uit de stack
    :param: self
    :return: top item of the stack
    :postconditie: er zit een element minder in de stack
    """
    def pop(self):
        return self.items.pop()

    """
    vraagt het laatst toegevoegde element uit de stack op
    :param: self
    :return: top item of the stack
    """
    def getTop(self):
        return self.items[-1]

