# Return a new list containing all elements from the original list, excluding the first and last elements
l1 = [1,2,3,4]
l2=[1,2,3,4,5]
l3=[10,13,44,55,66]
def medium_list(l11):
    return l11[1:-1]

result=medium_list(l1)
result2=medium_list(l2)
result3=medium_list(l3)
print(result)
print(result2)
print(result3)