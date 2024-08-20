dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}


def merge_dict(dict1,dict2):
    result = dict1.copy()     # Creates a shallow copy of the dicionary1 so no changes are done to the dictionary
    for k,v in dict2.items():
        result[k] = result.get(k,0)+v
    return result

result = merge_dict(dict1,dict2)
print(result)

# Time Complexity : The overall time complexity of this function is O(n + m),
# where n is the number of elements in dict1 and m is the number of elements in dict2.
# The copy() method takes O(n) time, and the loop iterates m times with O(1) operations inside the loop.


# Space complexity:
#
# The space complexity of this function is O(n + m) in the worst case, where all keys in dict1 and dict2 are distinct,
# and the merged dictionary has n + m elements. In the best case, where dict1 and dict2 have
# the same keys, the space complexity
# is O(n) (or O(m), whichever is larger), as the merged dictionary has the same number of elements as the input dictionaries.