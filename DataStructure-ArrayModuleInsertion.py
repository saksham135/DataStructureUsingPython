# we will insert the elemnts in the array at different places in an array that is inbuilt in python

from array import *

my_array1=array('i',[10,20,30,40,50])

print('Before Insertion:',my_array1)

# Insertion at Beginning .
# we will insert a new element at the Beginning of the Array using
# the insert method that take two arguments insert(index,value)
# my_array1.insert(0,25)
# print("After Insertion In Starting",my_array1)

#Insertion at Middle .
# we will insert a new element in the middle of array at some
# position and the elements from that position will be shifted 1 step towards right .
# my_array1.insert(3,100)
# print("After Inserting Element at Middle:",my_array1)



#Insertion at Last
# we will insert the new element at the last position .
my_array1.insert(100,110)
my_array1.insert(12,122)
print('After Inserting Element at the Last Position:',my_array1)