# Given two unsorted arrays of same size
# where arr[i] >= 0 for all i, the task is to check if
# two arrays are permutations of each other or not.


# Examples:
#
# Input: arr1[] = {2, 1, 3, 5, 4, 3, 2}
#        arr2[] = {3, 2, 2, 4, 5, 3, 1}
# Output: Yes
# Input: arr1[] = {2, 1, 3, 5}
#        arr2[] = {3, 2, 2, 4}
# Output: No
arr1= [2, 1, 3, 5, 4, 3, 2]
arr2= [3, 2, 7, 4, 5, 3, 1]
def find_permutation(list1,list2):
    if len(list1)!=len(list2):
        return False # if the length of both list is not equal then they are not permutation of each other
    list1.sort()
    list2.sort()
    if list1==list2:
        return True
    else:
        return False

result = find_permutation(arr1,arr2)
print(result)