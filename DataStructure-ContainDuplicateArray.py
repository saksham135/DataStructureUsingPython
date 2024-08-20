# Contains Duplicate
# Given an integer array nums, return true if any value appears at least
# twice in the array, and return false if every element is distinct.
#
# Example :
#
# Input: nums = [1,2,3,1]
# Output: true
# Hint: Use sets

# Method -1 :

nums = [1,2,3,1]

def find_duplicate(arr):
    seen = set()
    for i in arr:
        if i in seen:
            return True
        seen.add(i)
    return False

result = find_duplicate(nums)
print(result)
