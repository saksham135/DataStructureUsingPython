# Traversing refers to visit all the keys and values pair of dictionary exactly one

my_dict = {
    "name":"saksham",
    "age":20,
    "address":"jalandhar"
}


def traverse_dict(dict1):
    for i in dict1:
        print(f'The Value for the key {i} is {dict1[i]}')

traverse_dict(my_dict)


# Time Complexity = O(n) where n is the number of elements
# Space Complexity = O(1) 