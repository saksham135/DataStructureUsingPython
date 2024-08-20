class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofstring = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        current = self.root
        for i in word:
            ch=i
            node = current.children.get(i)
            if node==None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endofstring=True
        print('Node Inserted Successfully')

    def search(self,word):
        current = self.root
        for i in word:
            node = current.children.get(i)
            if node==None:
                return False
            current = node
        if current.endofstring==True:
            return True
        else:
            return False

    def deletestring(root,word,index):
        ch = word[index]
        current = root.children.get(ch)
        canthisnnodebedeleted = False
        if len(current.children)>1:




newTrie = Trie()
newTrie.insert('Apple')
newTrie.insert('Appi')
print(newTrie.search('Apple'))


