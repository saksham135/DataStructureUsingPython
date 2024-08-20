import QueueUsingLL as queue

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.Lchild = None
        self.Rchild = None


newBT = TreeNode('Drinks')
LeftChild = TreeNode('Hot')
tea = TreeNode('Tea')
coffee = TreeNode('Coffee')
LeftChild.Lchild = tea
LeftChild.Rchild = coffee
RightChild = TreeNode('Cold')
Cola = TreeNode('Cola')
Fanta = TreeNode('Fanta')
RightChild.Lchild = Cola
RightChild.Rchild = Fanta
newBT.Lchild = LeftChild
newBT.Rchild = RightChild


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

def postorder(rootnode):
    if not rootnode:
        return
    postorder(rootnode.Lchild)
    postorder(rootnode.Rchild)
    print(rootnode.data)

def levelorder(rootnode):
    if not rootnode:
        return
    else:
        myqueue = queue.Queue()
        myqueue.enqueue(rootnode)
        while not (myqueue.isempty()):
            root = myqueue.deqeue()
            print(root.value.data)
            if (root.value.Lchild is not None):
                myqueue.enqueue(root.value.Lchild)
            if (root.value.Rchild is not None):
                myqueue.enqueue(root.value.Rchild)




def search_node(rootnode,nodevalue):
    if not rootnode:
        return 'The Bt Does not Exist'
    else:
        customqueue = queue.Queue()
        customqueue.enqueue(rootnode)
        while not(customqueue.isempty()):
            root = customqueue.deqeue()
            if root.value.data == nodevalue:
                return 'Success'
            if (root.value.Lchild) is not None:
                customqueue.enqueue(root.value.Lchild)
            if (root.value.Rchild) is not None:
                customqueue.enqueue(root.value.Rchild)
        return 'Not Found'

def insertnode(rootnode,newnode):
    if not rootnode:
        rootnode = newnode
    else:
        customqueue = queue.Queue()
        customqueue.enqueue(rootnode)
        while not(customqueue.isempty()):
            root = customqueue.deqeue()
            if root.value.Lchild is not None:
                customqueue.enqueue(root.value.Lchild)
            else:
                root.value.Lchild = newnode
                return 'Sucessfully Inserted'
            if root.value.Rchild is not None:
                customqueue.enqueue(root.value.Rchild)
            else:
                root.value.Rchild = newnode
                return 'Sucessfully Inserted'





newdrink = TreeNode('HOTDRINKS')
print(insertnode(newBT,newdrink))
levelorder(newBT)