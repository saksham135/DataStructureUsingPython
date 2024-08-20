# A Tuple is an inmutuable sequence of python objects .
# new_tuple = ('a','b','c','d')
# # print(new_tuple)
# new_tuple1 = ('a',)
# print(new_tuple1)
#
# new_tuple = tuple('abcda')
# print(new_tuple)


# Tuples are inmutuable which means once you declared you cannot change them and they stay as it is .

# new_tuple = ('a','b','c','d','e')
#
# print(new_tuple[1])
# print(new_tuple[-1])
# print(new_tuple[-2])



# Slice Operator :

# syntax : tuple[leftIndex:rightIndex]

# new_tuple = (1,2,3,4,5)

# print(new_tuple[1:3])
# print(new_tuple[0:3])
# print(new_tuple[:3])
# print(new_tuple[:])

# Traversing a tuple

# for i in new_tuple:
#     print(i)                     # time complexity = O(n)
#                                  # space complexity = O(1)

# searching an element in tuple

# method-1
# print('f' in new_tuple)         # Time complexity = O(n)
# print(3 in new_tuple)

# method -2

# def search_elem(tuple1,element):
#     for i in range(len(tuple1)):
#         if tuple1[i]==element:
#             return f"Element found in tuple at index {i}"
#     return f"Element is not Present in the Tuple"
#
# print(search_elem(new_tuple,6))
# print(search_elem(new_tuple,4))

# Time complexity = O(n)
# Space complexity = O(1)

# method-3 using index method
# print(new_tuple.index(2))
# # print(new_tuple.index(6))

# Time complexity = O(n)

# Tuple Operations / Functions

myTuple=(1,4,3,2,5)
myTuple1=(1,2,6,9,8,7)

# print(myTuple+myTuple1)
# print(6 in myTuple)
# print(3 in myTuple)
# print(myTuple.count(3))
# print(myTuple.index(2))
# print(len(myTuple))
# print(max(myTuple1))
L1 = [1,2,3,4,5]
print(tuple(L1))

