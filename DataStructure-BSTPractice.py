class Treenode:
    def __init__(self,data):
        self.data = data
        self.Lchild = None
        self.Rchild = None


def insertnode(rootnode,value):
    if rootnode.data is None:
        rootnode.data = value
    elif value<rootnode.data:
        if rootnode.Lchild is None:
            rootnode.Lchild.data = Treenode(value)
        else:
            insertnode(rootnode.Lchild,value)
    elif value>rootnode.data:
        if rootnode.Rchild is None:
            rootnode.Rchild.data = Treenode(value)
        else:
            insertnode(rootnode.Rchild,value)
    return 'The Node has been succesfully inserted'



