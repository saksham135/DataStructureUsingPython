list1= [1,3]
list2=[2]

def find_median(l1,l2):
    # creating a new list l3 that is sum of l1 and l2
    new_list = l1+l2

    #sorted the new_list
    new_list.sort()

    #finding the lenght of the list
    my_length = len(new_list)

    # if the length of list is odd set the middle elements as the median
    if my_length%2==1:
        return float(new_list[my_length//2])
    else:
        middle1 = new_list[my_length//2-1]
        middle2 = new_list[my_length//2]
        return float((middle1)+(middle2)/2)

result =find_median(list1,list2)
print('Median is:',result)