# Merge Two Sorted Linked List
# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.
#
# Example 1:
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
#
# Output: [1,1,2,3,4,4]

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        current = self.head
        result = ''
        while current is not None:
            result+=str(current.value)
            if current is not None:
                result+='->'
            current = current.next
        return result

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1

    def merge_linkedlists(self,l1,l2):
        prehead = Node(-1)
        prev = prehead
        while l1 and l2:
            if l1.val<=l2.val:
                prehead.next = l1
                l1=l1.next
            else:
                prehead.next = l2
                l2 = l2.next
        prev.next=l1 if l1 is not None else l2
        return prehead.next



n_l_l = LinkedList()
n_l_l.append(10)
n_l_l.append(20)
n_l_l.append(30)
n_l_l.prepend(5)
n_l_l.prepend(1)
print(n_l_l)

l2 = LinkedList()
l2.append(10)
l2.append(20)
l2.append(40)
print(l2)