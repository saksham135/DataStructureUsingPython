# Searching refers to finding a specific key value pair in the dictionary which requires iterating through the dictionary
# and checking whether the given value macthes with value in the dictionary if it we return true otherwise false .
my_dict ={
    "name":"saksham",
    "age":20,
    "address":"jalandhar"
}


def search_dict(dict1,value):
    for i in dict1:
        if dict1[i]==value:
            return i,value
    return 'The Value does not exist'

# element = (int(input('Enter the specific key that you want to search in the dictionary:')))
result = search_dict(my_dict,'saksham')
print(result)

# Time complexity is O(n) where n is the number of elements
# Space complexity is O(1)