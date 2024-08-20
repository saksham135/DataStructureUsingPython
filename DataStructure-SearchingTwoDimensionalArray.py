# we will search a given element in the two dimensional Array .
# if it is found we will return the message of element found otherwise we will return element not found message .


from numpy import *



array1 = array ([[10,20,30,40],[50,60,70,80],[90,100,110,120],[130,140,150,160]])
print(array1)


def searchtwodimensionalarray(arr1,target):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            if (arr1[i][j] == target):
                return 'The Value is located at index'+str(i)+" "+str(j)
            else:
                return 'The Element is not Found'


user_input=(int(input('Enter the target value to be searched inside the array:')))
searchtwodimensionalarray(array1,user_input)



#Time Complexity of search operation is O(n^2) if number of column and no of rows are same .
# otherwise it is O(m*n) where m is number of columns and n is number of rows .
#Space Complexity is O(1)