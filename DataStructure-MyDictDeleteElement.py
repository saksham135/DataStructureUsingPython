# We will delete the element from the list using 3 methods
# 1. Using del keyword
# 2. Using Pop Method
# 3. Using popitem method
# 4. using clear method to delete whole dictionary

my_dict = {
    "name":"saksham",
    "age":20,
    "address":"jalandhar"
}



#1 Using del keyword

# del my_dict["age"]
# print(my_dict)


# Time Complexity - O(1)
# Space Complexity - O(1)

# 2 Using pop() method- Here pop() method requires the key and cannot be empty

# removed_element = my_dict.pop('age')
# print(removed_element)
# print(my_dict)

# Time Complexity - O(1)
# Space Complexity - O(1)

#3. Using popitem method - can be empty and randomly delete a key ,value pair
# removed_element = my_dict.popitem()
# print(my_dict)

# Time complexity - O(1)
# Space complexity - O(1)

#4. Using clear method - clear method will delete the whole dictionary
my_dict.clear()
print(my_dict)

# Time Complexity- O(n)
# Space Complexity - O(1)


