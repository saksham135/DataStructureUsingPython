# A Dictionary is mutuable collection of key,value pairs where each unique key maps to the value .

# Creating an Empty Dictionary .


# Method-1 Using Constructor -

# my_dict = dict()
# print(my_dict)

# Method 2 - Using Paranthesis

# my_dict1 = {}
# print(my_dict1)

# Time Complexity of Both Cases is O(1)
# Space Complexity of Both Cases is O(1).


# Dictionary Syntax :  my_dict = dict(key1='value',key2='value',key3='value3)

# creating dictionary using 3 methods
# 1. Using Dictionary Constructor
# 2. Using {}
# 3. Using Tuple and Dictionary constructor

# using Constructor :
# my_dict = dict(one='uno',two='dos',three='tres')
# print(my_dict)

# Both the Time and Space Complexity is O(n)
# Time complexity is O(n) since we have to allocate space for storing the n number of elements
# Space complexity is O(n) since we have to allocate the space inside the memory to store all the n elements.

# using {}
# my_dict  = {
#     'one':'uno',
#     'two':'dos',
#     'three':'tres'
# }
# print(my_dict)

# Both the time complexity and space complexity is
# Time complexity is O(n) since we have to allocate space for storing the n number of elements
# Space complexity is O(n) since in memory space will be allocated for both the kry value pair .

# using the Tuple Method
# we have first initialized the tuple and then we have converted it back into the dictionary using dict constructor.
# my_list_of_tuple = [('key1','value1'),('key2','value2'),('key3','value3')]
# print(dict(my_list_of_tuple))

eng_sp_3 = [('one','uno'),('two','dos'),('three','tres')]
print(dict(eng_sp_3))

# Time complexity is O(n)
# Space complexity is O(n)


# Dictionaries In Memory :
# Dictionary are generally implemented using the hash tables .
# A Hash Table is a way of doing key value look ups.
# Hash Table consist of :
# 1. The Keys
# 2. The array
# 3. The Hash Function