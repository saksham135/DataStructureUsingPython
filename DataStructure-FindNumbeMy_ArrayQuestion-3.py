# creating a numpy array

import numpy as np

my_array  = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

def search_array(arr1,target):
    for i in range(len(arr1)):
        if arr1[i] == target:
            return True
    return False


my_value = (int(input('Enter the value to be searched inside the array')))
result = search_array(my_array,my_value)
if result == True:
    print(f'{my_value} exists in the given array of size {len(my_array)}')
elif result == False:
    print(f'{my_value} does not exist in the array.')