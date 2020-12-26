import Tree

class BSTTable():
    def __init__(self):
        self.BST = Tree.BST()

    def tableIsEmpty(self):
        return self.BST.isEmpty()

    def tableInsert(self, item):
        return self.BST.searchTreeInsert(item)

    def tableRetrieve(self, key):
        return self.BST.searchTreeRetrieve(key)

    def traverseTable(self, print):
        self.BST.inorderTraverse()

    def save(self):
        return self.BST.save()
    
    def load(self, tree):
        return self.BST.load(tree)

    def tableDelete(self, key):
        return self.BST.searchTreeDelete(key)

t = BSTTable()
print(t.tableIsEmpty())
print(t.tableInsert(Tree.createTreeItem(8,8)))
print(t.tableInsert(Tree.createTreeItem(5,5)))
print(t.tableIsEmpty())
print(t.tableRetrieve(5)[0])
print(t.tableRetrieve(5)[1])
t.traverseTable(print)
print(t.save())
t.load({'root': 10,'children':[{'root':5},None]})
t.tableInsert(Tree.createTreeItem(15,15))
print(t.tableDelete(0))
print(t.save())
print(t.tableDelete(10))
print(t.save())