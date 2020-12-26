def createTreeItem(key,val):
    node = BST()
    node.key = key
    node.val = val
    return node

class BST:
    def __init__(self):
        self.key = None
        self.val = None
        self.right = None
        self.left = None

    def isEmpty(self):
        if (self.key is None):
            return True
        return False
    
    def searchTreeInsert(self, item):
        if self.key is None:
            self.key = item.key
            self.val = item.val
            return True

        if self.key < item.key:
            if self.right is None:
                self.right = item
                return True
            self.right.searchTreeInsert(item)
        else:
            if self.left is None:
                self.left = item
                return True
            self.left.searchTreeInsert(item)
        
    def searchTreeRetrieve(self, key):
        if self.key == key:
            return [self.key, True]
            
        if self.key < key:
            return self.right.searchTreeRetrieve(key)
        else:
            return self.left.searchTreeRetrieve(key)

    def inorderTraverse(self, val=1):
        if self.left is not None:
            self.left.inorderTraverse(self.left)

        print(self.key)

        if self.right is not None:
            self.right.inorderTraverse(self.right)
    
    def inorder_sucessor(self, start = True):
        if start:
            if self.right.left is None:
                r = self.right
                self.right = None
                return r

            self.right.inorder_sucessor(False)
        
        if self.left.left is None:
            r = self.left
            self.left = None
            return r

        self.left.inorder_sucessor(False)
    
    def searchTreeDelete(self, key):
        try:
            self.searchTreeRetrieve(key)
        except:
            return False
        
        if self.key == key:
                self.key = self.inorder_sucessor().key
                return True
        elif self.left.key == key:
            if self.left.left is None and self.left.right is None:
                self.left = None
                return True
            elif self.left.left is None ^ self.left.right is None:
                if self.left.left:
                    self.left = self.left.left
                else:
                    self.left = self.left.right
        elif self.right.key == key:
            if self.right.left is None and self.right.right is None:
                self.right = None
                return True
            elif self.right.left is None ^ self.right.right is None:
                if self.right.left:
                    self.right = self.right.left
                else:
                    self.right = self.right.right
        else:
            if self.key > key:
                self.left.searchTreeDelete(key)
            else:
                self.right.searchTreeDelete(key)

        return True

    def save(self, hash={}):
        hash["root"] = self.key

        if self.left is not None:
            hash["children"] = []
            hash["children"].append(self.left.save({}))
        elif self.right is not None:
            hash["children"] = []
            hash["children"].append(None)

        if self.right is not None:
            hash["children"].append(self.right.save({}))
        elif self.left is not None:
            hash["children"].append(None)
        
        return hash
    
    def load(self, tree, start = True):
        self.key = tree["root"]
        try:
            self.left = BST()
            self.left.load(tree["children"][0], False)
        except:
            self.left = None
        
        try:
            self.right = BST()
            self.right.load(tree["children"][1], False)
        except:
            self.right = None