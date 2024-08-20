# Dictionary Methods -

my_dict = {
    "name":"saksham",
    "age":20,
    "address":"jalandhar",
    "college":"Daviet"
}

#1. Clear() Method - It removes all the keys and values in the dictionary and returns an empty dictionary as output .
# my_dict.clear()
# print(my_dict)

#2. Copy Method - It Creates a shallow copy of the original dictionary instead of modifying or doing the change in the original one .
# Syntax - Dictionary.copy()
# new_dict = my_dict.copy()
# print(new_dict)


#3. fromkeys() - Creates a new dictionary and take value,pair

# syntax - dictionary.fromkeys(sequence[],values)

# new_dict = {}.fromkeys([1,2,3],0)   # we have given [1,2,3] as keys and 0 as values
# print(new_dict)

# if we donot give the values then it will provida none
# new_dict = {}.fromkeys([1,2,3])
# print(new_dict)

#4.get() - it takes the key and value if the key exist in dictionary then it will give the result
# otherwise it will return the value given as the parameter

# syntax - dictionary.get(key,value)

# print(my_dict.get("age",27))

# print(my_dict.get("city",29))

#5.items() method -  return the list of all the key and values separated by tuple in pair in form of whole list .

# syntax - dictionary.items()
# print(my_dict.items())

#6. keys() method - returns all the keys in given dictionary in form of list .
# print(my_dict.keys())

#7.popitems() method -  delete any random key value pair from the original dictionary

# syntax - dictionary.popitem()

# my_dict.popitem()
# print(my_dict)

#8.setdefault() method - checks for the key if the given exist in dictionary it returns that key value
#otherwise it will return the value in other case it will add key and value as new in the dictionary.

# syntax - dictionary.setdefault(key,offset_value)

# print(my_dict.setdefault("age",30))
# print(my_dict.setdefault("added",35))
# print(my_dict)

#9.pop() method - removes the specific key and value from the dictionary

# syntax - dictionary.pop(key,default_value)

# my_dict.pop("age")
# print(my_dict)

#10.values method() - return all the values in the given dictionary
# syntax  - dictionary.values()
# print(my_dict.values())

#11.update method()- add the new dictionary to the current dictionary

# syntax - dictionary.update(new_dictionary)
new_dict = {
    1:"a",
    2:"b",
    3:"c"
}

my_dict.update(new_dict)
print(my_dict)

