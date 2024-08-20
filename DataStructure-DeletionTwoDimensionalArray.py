# we will delete the existing row or column from a two dimensional array .
# since in a two dimensional array we can delete only one element .



from numpy import *



arr1 =  array([[10,20,30,40],[50,60,70,80],[90,100,110,120],[130,140,150,160]])
print(arr1)
n_array = delete(arr1,0,axis=0)

print(n_array)

# Time complexity of deleting the existing row or column
# from the array is O(m*n) where m is number of column and n is number of rows .
# if the number of rows and columns are equal then it is O(n^2).
# Space complexity is also O(1) since we need to maintain new array for storing it as well.

