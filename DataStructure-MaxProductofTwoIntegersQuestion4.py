
elem = (int(input('Enter the total number of elements to be input inside array')))

my_array = []

for i in range(elem):
    inp = (int(input(f'Enter the Element {i+1} to be input at index{i}')))
    my_array.append(inp)
    # my_array.sort(reverse=True)

print('Elements in the list are:',my_array)

# def max_product(list1):
#     for i in range(len(list1)):
#         for j in range(i+1,len(list1)):
#             return list1[i]*list1[j]
#
# result = max_product(my_array)
# print(f'The Maximum Product of Two integers in a given array is {result}


# Method-2

def max_array(arr):
    # Initialize Two Variables max1 and max2 with 0
    max1,max2 =0,0

    for i in arr :
        if i >max1:
            max2 = max1
            max1 = i
        elif i>max2:
            max2 = i
    return max1*max2

result = max_array(my_array)
print(result)