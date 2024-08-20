my_list = [10,20,30,40,50,60]
target = (int(input('Enter the Element to be searched inside the list :')))

# -------------------------------------------------------------Method1:Using the in keyword.
# if target in my_list:
#     print(f'{target} is present in list.')
# else:
#     print(f'{target} is not present in the list.')


#                                                Time complexity -In Worst Case- O(n)
#                                                where n is the total number of elements .
#                                                Average Case Complexity is O(1)

# -------------------------------------------------------------Method2: Using for loop or enumerate function

#                                                 Case1-Using for loop and if statement

# def search(list1,element):
#     for i in range(len(list1)):
#         if list1[i]==element:
#             print(f'{element} is present in list at index {i}')
#         else:
#             print(f'{element} is not present in the list')
#
#
# search(my_list,target)


def search(list1,element):
    for i,value in enumerate(list1):
        if value==element:
            return 1
    return -1


print(search(my_list,target))


#Time complexity - O(n)
# Space complexity - O(1)