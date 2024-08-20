# input_num = (int(input('Enter How Many Number elements you want in array:')))
# find_num = (int(input('Enter the Missing Number to be Searched Inside the Given Array:')))
#
# my_array = []
# for j in range(input_num):
#     my_array.append(j)
#
#
# def missing_number(arr, n):
#     for i in range(len(arr)):
#         if arr[i] == n:
#             return True
#     else:
#         return False
#
#
#
# result = missing_number(my_array, find_num)
#
# if result == True:
#     print(f'{find_num} is Present in the given array.')
# elif result == False:
#     print(f'{find_num} is not present in the array')

# Method -2
my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20]
input_num = (int(input('Enter the total number of elements in the list')))

def find_missing(arr,n):
    # calculate the sum of first n natural number sum using arithmetic progression formula n*(n+1)//2
    sum1 = n*(n+1)//2
    # find the sum of all the elements present in the list using sum function
    array_sum = sum(arr)
    #Find the missing number in list by subtracting the total sum of n numbers with sum of all elements in list
    missing  = sum1-array_sum
    print(f'{missing} is the missing number in the array.')

find_missing(my_list,input_num)

