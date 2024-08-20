# we will traverse the two dimensional array in which we will visit each element one by one and will print it.


from numpy import *



arr2=array([[10,20,30,40],[50,60,70,80],[90,100,110,120]])


def traversearray(arr1):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            print(arr1[i][j])

traversearray(arr2)


# Time complexity : o(n^2) if number of rows and columns are equal .
# otherwise O(m*n) if number of rows and columns are not equal.
#Space complexity is O(1) since no extra space is required.
