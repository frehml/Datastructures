class BST:
    """
    initializeerd een object BST
    :param: value=None, data=None
    :return: BST instansie
    """
    def __init__(self, value=None, data=None):
        self.value = value
        self.data = data
        self.right = None
        self.left = None

    """
    insert een node in de boom
    :param: value, data
    :return: void
    """
    def insert(self, value, data):
        if self.value is None:
            self.value = value
            self.data = data
            return

        if self.value < value:
            if self.right is None:
                self.right = BST(value, data)
                return
            self.right.insert(value, data)
        else:
            if self.left is None:
                self.left = BST(value, data)
                return
            self.left.insert(value, data)

    """
    loopt door de boom inorder en yields die nodes
    :param: val=1
    :yield: nodes
    """
    def inorder(self, val=1):
        if val is None:
            return

        if self.left is not None:
            yield from self.left.inorder(self.left)

        yield self

        if self.right is not None:
            yield from self.right.inorder(self.right)

    """
    Vindt een node in de boom met een value
    :param: val
    :return: node
    """
    def search(self, val):
        if self.value == val:
            return self.data
            
        if self.value < val:
            return self.right.search(val)
        else:
            return self.left.search(val)
    
    def save(self):
        pass
