class Heap:
    def __init__(self,size):
        self.customList = (size+1)*[None]
        self.heapSize = 0
        self.maxSize = size+1

def peek(rootnode):
    if not rootnode:
        return
    else:
        return rootnode.customlist[1]

def sizeofheap(rootnode):
    if not rootnode:
        return
    else:
        return rootnode.heapSize

def levelordertraversal(rootnode):
    if not rootnode:
        return
    else:
        for i in range(1,rootnode.heapSize+1):
            print(rootnode.customList[i])

def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)

def inserNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary Heap is Full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "The value has been successfully inserted"

def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return

    else:
        if heapType == "Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
    heapifyTreeExtract(rootNode, swapChild, heapType)


def extractnode(rootnode,heapType):
    if not rootnode:
        return
    else:
        extractednode = rootnode.customlist[1]
        rootnode.customList[1]=rootnode.customList[rootnode.heapSize]
        rootnode.customList[rootnode.heapSize]=None
        rootnode.heapSize-=1
        heapifyTreeExtract(rootnode,1,heapType)
        return extractednode

def deleteEntireTree(rootnode):
    rootnode.customList=None




newHeap = Heap(5)
inserNode(newHeap,1,"Min")
inserNode(newHeap,2,"Min")
inserNode(newHeap,3,"Min")
inserNode(newHeap,4,"Min")
# deleteEntireTree(newHeap)
levelordertraversal(newHeap)

