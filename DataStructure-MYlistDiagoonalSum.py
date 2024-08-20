# Given 2D list calculate the sum of diagonal elements.
# Example
#
# myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# diagonal_sum(myList2D)  # 15

import numpy as np
#Created a 2d array using numpy array module
my_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
# # print(my_array.shape)
#
# def add_diagonal(arr):
#     total = 0
#     for i in range(len(arr)):
#         total +=arr[i][i]
#     return total
#
# res1 = add_diagonal(my_array)
# print('The sum of the diagonal elements of the array is:',res1)
#
# # It only add the Elements of Rows and Columns which have same index
# # i.e value of both i in line 16 is same and that element is picked and added to the total element .
# #  example arr[0][0],arr[1][1]

# random_array_2 = np.random.randint(100,size=(5,5))
# print(random_array_2)
# print(len(random_array_2))

def find_diagonal(mat):
    row = len(mat)
    total = 0
    for i in range(row):
        total+=mat[i][i]+mat[i][row-i-1]
    return total-mat[row//2]-mat[row//2] if total%2!=0 else total

result=find_diagonal(my_array)
print('The Diagonal Matrix Sum is',result)