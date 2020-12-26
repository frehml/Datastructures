class Stack:
    """
    creert een lege stack
    :param: self
    :return: Stack
    :postconditie: je krijgt een stack terug
    """
    def __init__(self):
        self.top = None
        self.next = None

    """
    bepaalt of een stack leeg is
    :param: self
    :return: bool
    """
    def isEmpty(self):
        if(self.top is None):
            return True
        return False

    """
    voegt een element toe aan de stack
    :param: self, el
    :return: void
    :postconditie: er zit een ele meer in de stack
    """
    def push(self, ele):
        s = Stack()
        s.top = self.top
        s.next = self.next

        self.next = s
        self.top = ele
        return True
    
    """
    verwijdert het laatst toegevoegde element uit de stack
    :param: self
    :return: top item of the stack
    :postconditie: er zit een element minder in de stack
    """
    def pop(self):
        if (self.isEmpty()):
            return [None, False]
        
        popped = self.top
        self.top = self.next.top
        self.next = self.next.next
        return [popped, True]

    """
    vraagt het laatst toegevoegde element uit de stack op
    :param: self
    :return: top item of the stack
    """
    def getTop(self):
        if (self.isEmpty()):
            return [None, False]
        
        return [self.top, True]

    
    def load(self, array):
        self.top = None
        self.next = None

        for i in array:
            self.push(i)
    
    def save(self):
        arr = []
        while (not self.isEmpty()):
            arr.append(self.pop()[0])
        
        self.load(arr[::-1])
        return arr[::-1]

s = Stack()
print(s.isEmpty())
print(s.getTop()[1])
print(s.pop()[1])
print(s.push(2))
print(s.push(4))
print(s.isEmpty())
print(s.pop()[0])
s.push(5)
print(s.save())
s.load(['a','b','c'])
print(s.save())
print(s.pop()[0])
print(s.save())
print(s.getTop()[0])
print(s.save())

#True
#False
#False
#True
#True
#False
#4
#[2,5]
#['a','b','c']
#c
#['a','b']
#b
#['a','b']