# Accessing any Given Element from the array for which we will ask index
# from the user and will use it with the array name for accessing the element .

# we will import the array module

from array import *

my_array1 = array('i',[20,30,40,50,60])

def accesselement(index,array):
    if index>=len(array):
        print('Sorry , But Index out of Range')
    else:
        print(f"The Element at the Given Index is {array[index]}")


u_index = (int(input('Enter The Index for Accessing the Element from Array:')))
accesselement(u_index,my_array1)

# Time Complexity for Accessing the Element from the Given Array is O(1).
# Space Complexity for Accessing the Element from the Given Array is O(1).