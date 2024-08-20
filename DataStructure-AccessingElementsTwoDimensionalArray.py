# we will access the elements from the two dimensional array by giving the row and column index

from numpy import *

array_1 = array([[10,20,30,40],[50,60,70,80],[90,100,110,120]])

print(array_1)
def accessarray(arr1,r_index,c_index):
    if r_index>=len(arr1) or c_index>=len(arr1[0]):
        print('Index Out of Range')
    else:
        print(arr1[r_index][c_index])


row_index=(int(input('Enter the row index to access the element of specific row')))
column_index=(int(input('Enter the column index to access the element of the specific column')))

accessarray(array_1,row_index,column_index)

# Time complexity - So the Time Complexity for accessing the Element of the 2d array is O(1)
# Space complexity - Space complexity for accessing the Element of 2d Array is O(1).