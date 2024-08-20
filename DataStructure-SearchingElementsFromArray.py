# Searching an Element from the Given Array we will use the linear search .

from array import *

my_array1 = array('i',[10,20,30,40,50])

def searcharray(arr,target):
    for j in range(len(arr)):
        if arr[j]==target:
            print(f"Element Found at Index {j}")
    return -1


value = (int(input("Please Enter the value to search inside the Array:")))

searcharray(my_array1,value)


# Time complexity for searching an element from the n elements using linear search is O(n).
# Space complexity for searching an element from the n elements is O(1).