#Duplicate Number
#Write a function to remove the duplicate numbers on given integer array/list.

#Example

#remove_duplicates([1, 1, 2, 2, 3, 4, 5])
#Output : [1, 2, 3, 4, 5]

my_list  = [1,1,2,2,3,4,5]

# def remove_duplicate(arr):
#     arr = list(set(arr))
#     return arr
#
#
# result = remove_duplicate(my_list)
# print(result)

# in method 1 we have used set method to convert the array into the set since set does not support the duplicates
# then we have converted it back into the list and returned and printed it


def remove_duplicates(arr):
    n_l = []
    seen = set()
    for i in arr:
        if i not in seen:
            n_l.append(i)
            seen.add(i)
    return n_l

result = remove_duplicates(my_list)
print(f'The Original List after removing all the duplicates are {result}')


#Time complexity analysis:

#Creating an empty list unique_lst: O(1)

#Creating an empty set seen: O(1)


#Looping through the input list lst of length n: O(n)

# For each item, checking if the item is in the set seen: O(1) on average
#
# If the item is not in the set, appending it to the list unique_lst: O(1) on average
#
# Adding the item to the set seen: O(1) on average
# 
# Returning the list unique_lst: O(1)
#
# Overall time complexity: O(n)
#
# The loop iterates through the entire list once, and the set operations (lookup, add)
# inside the loop have an average time complexity of O(1). Therefore, the overall time complexity is O(n).
#
# Space complexity:
#
# O(n), as we're using additional data structures (list and set) to store unique elements.

