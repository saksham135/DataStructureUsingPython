import QueueUsingLL as queue
class BSTNODE:
    def __init__(self,data):
        self.data = data
        self.Lchild = None
        self.Rchild = None

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.Lchild is None:
            rootNode.Lchild = BSTNODE(nodeValue)
        else:
            insertNode(rootNode.Lchild, nodeValue)
    else:
        if rootNode.Rchild is None:
            rootNode.Rchild = BSTNODE(nodeValue)
        else:
            insertNode(rootNode.Rchild, nodeValue)
    return "The node has been successfully inserted"


def preorder(rootnode):
    if not rootnode:
        return
    else:
        print(rootnode.data)
        preorder(rootnode.Lchild)
        preorder(rootnode.Rchild)

def inorder(rootnode):
    if not rootnode:
        return
    inorder(rootnode.Lchild)
    print(rootnode.data)
    inorder(rootnode.Rchild)

def postorder(rootnode):
    if not rootnode:
        return
    postorder(rootnode.Lchild)
    postorder(rootnode.Rchild)
    print(rootnode.data)

def levelorder(rootnode):
    if not rootnode:
        return
    customqueue = queue.Queue()
    customqueue.enqueue(rootnode)
    while not(customqueue.isempty()):
        root =customqueue.deqeue()
        print(root.value.data)
        if (root.value.Lchild) is not None:
            customqueue.enqueue(root.value.Lchild)
        if (root.value.Rchild) is not None:
            customqueue.enqueue(root.value.Rchild)


def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.Lchild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.Lchild, nodeValue)
    else:
        if rootNode.Rchild.data == nodeValue:
            print("The value is found")
        else:
            searchNode(rootNode.Rchild, nodeValue)

def minnode(bstnode):
    current = bstnode
    while current.Lchild is not None:
        current = current.Lchild
    return current

def deletenode(rootnode,value):
    if rootnode is None:
        return rootnode
    if value<rootnode.data:
        rootnode.Lchild = deletenode(rootnode.Lchild,value)
    elif value>rootnode.data:
        rootnode.Rchild = deletenode(rootnode.Rchild,value)
    else:
        if rootnode.Lchild is None:
            temp = rootnode.Rchild
            rootnode = None
            return temp

        if rootnode.Rchild is None:
            temp = rootnode.Lchild
            rootnode = None
            return temp

        temp = minnode(rootnode.Rchild)
        rootnode.data = temp.data
        rootnode.Rchild = deletenode(rootnode.Rchild,temp.data)
    return rootnode

def delete_all_node(rootnode):
    rootnode.data = None
    rootnode.Lchild = None
    rootnode.Rchild = None
    return 'The Bst has been deleted successfully'



newBST = BSTNODE(None)
insertNode(newBST,70)
insertNode(newBST,60)
insertNode(newBST,90)
insertNode(newBST,100)
insertNode(newBST,30)
delete_all_node(newBST)
levelorder(newBST)