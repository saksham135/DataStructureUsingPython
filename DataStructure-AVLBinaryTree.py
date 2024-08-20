class TreeNode:
    def __init__(self,data):
        self.data = data
        self.Lchild = None
        self.Rchild = None


def insertnode(rootnode,value):
    if rootnode.data==None:
        rootnode.data = value
    elif value<=rootnode.data:
        if rootnode.Lchild is None:
            rootnode.Lchild = TreeNode(value)
        else:
            insertnode(rootnode.Lchild,value)
    else:
        if rootnode.Rchild is None:
            rootnode.Rchild = TreeNode(value)
        else:
            insertnode(rootnode.Rchild,value)
    return 'The Node has been inserted Succesfully.'

def preorder(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preorder(rootnode.Lchild)
    preorder(rootnode.Rchild)

def inorder(rootnode):
    if not rootnode:
        return
    inorder(rootnode.Lchild)
    print(rootnode.data)
    inorder(rootnode.Rchild)

newBT = TreeNode(None)
insertnode(newBT,70)
insertnode(newBT,60)
insertnode(newBT,90)
insertnode(newBT,100)
insertnode(newBT,30)
preorder(newBT)