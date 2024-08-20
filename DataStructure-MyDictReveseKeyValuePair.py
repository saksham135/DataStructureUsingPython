my_dict = {'a': 1, 'b': 2, 'c': 3}


def rev_pair(dict1):
    return {v:k for k,v in dict1.items()}


result = rev_pair(my_dict)
print(result)