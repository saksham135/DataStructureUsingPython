my_dict = {
    3:"three",
    5:"five",
    9:"nine",
    2:"two",
    1:"one",
    4:"four"
}


# 1. In/Not Operator() -

# In operator works by default only for keys

#Case1:For Keys

# print(3 in my_dict)
# print(12 in my_dict)

# case 2 : for values
#
# print("three" in my_dict.values())
# print("fifteen" in my_dict.values())

# print("three" not in my_dict.values())
# print(3 not in my_dict)

# Case 2: len() function : used to check the length of the dictionary

# print(len(my_dict))

#2. all function() -

# case1 : all keys are true
#
# print(all(my_dict))

# case2: all keys are false

# my_dict1 = {
#     0:"three",
#     0:"five",
#     0:"nine",
#     0:"two",
#     0:"one",
#     0:"four"
# }
# print(all(my_dict1))

# case 3: one key is true

# new_dict  = {
#     1:"one",
#     False:"false"
# }
#
#
# print(all(new_dict))

# case 4: one key is false

# new_dict = {
#     0:"one",
#     False:"false"
# }
#
# print(new_dict)

#3-any () function  -

#case 1: all key are true
# print(any(my_dict))

# case2: one key is false
# new_dict = {
#     0:"one",
#     3:"three",
#     5:"five",
#     9:"nine",
#     2:"two",
#     1:"one",
#     4:"four"
#
# }
#
# print(any(new_dict))

# case 3: sorted() function -
print(sorted(my_dict))