class BinaryTree:
    def __init__(self,size):
        self.customlist = size*[None]
        self.lastusedindex = 0
        self.maxsize = size

    def insert(self,value):
        if self.lastusedindex+1==self.maxsize:
            return 'The Binary Tree is Full'
        self.customlist[self.lastusedindex+1]=value
        self.lastusedindex+=1
        return 'The Value Has Been Succesfullly Inserted'

    def search(self,nodevalue):
        for i in range(len(self.customlist)):
            if self.customlist[i]==nodevalue:
                return 'Success'
        return 'Not Found'

    def preorder(self,index):
        if index>self.lastusedindex:
            return
        print(self.customlist[index])
        self.preorder(index*2)
        self.preorder(index*2+1)

    def inorder(self,index):
        if index>self.lastusedindex:
            return
        self.inorder(index*2)
        print(self.customlist[index])
        self.inorder(index*2+1)

    def postorder(self,index):
        if index>self.lastusedindex:
            return
        self.postorder(index*2)
        self.postorder(index*2+1)
        print(self.customlist[index])

    def levelorder(self,index):
        for i in range(index,self.lastusedindex+1):
            print(self.customlist[i])

    def deletenode(self,value):
        if self.lastusedindex==0:
            return 'No Node to delete'
        for i in range(1,self.lastusedindex+1):
            if self.customlist[i]==value:
                self.customlist[i]=self.customlist[self.lastusedindex]
                self.customlist[self.lastusedindex]=None
                self.lastusedindex-=1
                return 'The Node Has Been Succesfully Deleted'

    def deleteall(self):
        self.customlist=None
        return 'The BST Has been succesfully Deleted'



newBT =BinaryTree(8)
newBT.insert('Drinks')
newBT.insert('Hot')
newBT.insert('Cold')
newBT.insert('Coffee')
newBT.insert('Tea')
newBT.insert('Cola')
newBT.insert('Fanta')
newBT.deletenode('Cola')
newBT.deleteall()
newBT.levelorder(1)
