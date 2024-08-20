import QueueUsingLL as queue
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.Lchild = None
        self.Rchild = None


newBT = TreeNode('Drinks')
LeftChild = TreeNode('Hot')
coffee = TreeNode('Coffee')
Tea = TreeNode('Tea')
LeftChild.Lchild = coffee
LeftChild.Rchild = Tea
RightChild = TreeNode('Cold')
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


def levelOrder(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isempty()):
            root = customQueue.deqeue()
            print(root.value.data)
            if (root.value.Lchild is not None):
                customQueue.enqueue(root.value.Lchild)

            if (root.value.Rchild is not None):
                customQueue.enqueue(root.value.Rchild)
def search(rootnode,value):
    if not rootnode:
        return
    else:
        myqueue = queue.Queue()
        myqueue.enqueue(rootnode)
        while not(myqueue.isempty()):
            root = myqueue.deqeue()
            if root.value.data == value:
                return 'Success'
            if (root.value.Lchild) is not None:
                myqueue.enqueue(root.value.Lchild)
            if (root.value.Rchild) is not None:
                myqueue.enqueue(root.value.Rchild)
        return 'Not Found'

def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isempty()):
            root = customQueue.deqeue()
            if root.value.Lchild is not None:
                customQueue.enqueue(root.value.Lchild)
            else:
                root.value.Lchild = newNode
                return "Successfully Inserted"
            if root.value.Rchild is not None:
                customQueue.enqueue(root.value.Rchild)
            else:
                root.value.Rchild = newNode
                return "Successfully Inserted"

def get_deepest(rootnode):
    if not rootnode:
        return
    else:
        cq = queue.Queue()
        cq.enqueue(rootnode)
        while not (cq.isempty()):
            root=cq.deqeue()
            if(root.value.Lchild) is not None:
                cq.enqueue(root.value.Lchild)
            if (root.value.Rchild):
                cq.enqueue(root.value.Rchild)
        deepest_node =root.value
        return deepest_node

def deletedeepestnode(rootnode,dNode):
    if not rootnode:
        return
    else:
        cq = queue.Queue()
        cq.enqueue(rootnode)
        while not(cq.isempty()):
            root = cq.deqeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.Rchild:
                if root.value.Rchild is dNode:
                    root.value.Rchild=None
                    return
                else:
                    cq.enqueue(root.value.Rchild)

            if root.value.Lchild:
                if root.value.Lchild is dNode:
                    root.value.Lchild = None
                else:
                    cq.enqueue(root.value.Lchild)

def delete_all(rootnode):
    rootnode.data = None
    rootnode.Lchild = None
    rootnode.Rchild = None
    return 'Binary Tree Deleted Successfully'


new_node = TreeNode('Cola')
insertNodeBT(newBT,new_node)

delete_all(newBT)
levelOrder(newBT)










