# we will remove the elements from the array from first , middle and last index using the remove method.

from array import *


my_array1=array('i',[10,20,30,40,50])

# my_array1.remove(10)
# print(my_array1)


# my_array1.remove(30)
# print(my_array1)

my_array1.remove(50)
print(my_array1)

#Time Complexity of Deleting an Element from the last is O(1).
#Time Complexity of Deleting an Element from the Middle is O(n) since we have to move each element by left for -1 position.
#Space Complexity of Deleting an Element from the Array is O(1).