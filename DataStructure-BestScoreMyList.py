#Best Score
#Given a list, write a function to get first, second best scores from the list.

#List may contain duplicates.

#Example

#myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
#first_second(myList) # 90 87


my_list  = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]

# My Method 1 -Short Method
# we will use python list set method to remove all the duplicates then we will use sort function wih reverse = true
# we will convert our list first into sets as set donot have duplicates then we will again convert it back to list and
# that will sort in in decending order and then we will print it out

# my_list = list(set(my_list))
# my_list.sort(reverse=True)
# print(my_list[0],my_list[1])


#Method 2

def best_score(arr):
    max1,max2 = float('-inf'),float('-inf')
    for num in arr:
        if num>max1:
            max2 = max1
            max1= num
        elif  num>max2 and num!=max1:
            max2 = num
    return max1,max2

result= best_score(my_list)
print(f'The Maximum score in the list are',result)


# Time complexity:
#
# The function iterates through the list my_list once,
# with each iteration taking constant time O(1) to perform comparisons and updates.
# Since there are n elements in the list, the overall time complexity of the function is O(n).

# Space complexity:
#
# The function uses a constant amount of additional space to store the variables
# max1 and max2. There are no other data structures or variables created that
# depend on the size of the input list. Therefore, the space complexity is O(1), as
# it remains constant regardless of the input size.