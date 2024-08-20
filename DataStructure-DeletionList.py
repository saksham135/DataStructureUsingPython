# We  will perform slicing and deletion operations on the list .


#--------------------------------------------------------------SLICING OPERATION--------------------------------------------------

my_list = ['a','b','c','d','e']
# print(my_list[0:2])
# print(my_list[:4])
# print(my_list[:])
# print(my_list[1:])


#----------------------------------------------------------------DELETION OPERATION-----------------------------------------------

# we will perform the deletion operation from the list by using 3 list methods :




#                                                                 1.pop()
# my_list.pop()
# my_list.pop(1)
# print(my_list)

# pop methods takes the index if index not given it will delete the last element from list .

#                                                                 2.delete()

# del my_list[1]
# print(my_list)

# delete method also take the index and it use [] brackets and it is used using del keyword.


#                                                                   3.remove()
# my_list.remove('a')
# my_list.remove('e')
# print(my_list)

# remove () method takes the element itself as the argument and delete the element .


# Time complexity -
# 1.pop()
             #pop()- Time complexity without parameter-O(1)
             #pop(index)- Time complexity with parameter - O(n)
# Space complexity - O(1)

# 2.del-
               # Time complexity - O(n)
               # Space complexity - O(1)

# 3.remove()-

               # Time complexity - O(n)
               # Space complexity - O(1)





