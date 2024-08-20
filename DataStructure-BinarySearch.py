from math import *

cs = [10,20,40,50,60,70,80,90,100]
def binarysearch(array,value):
    start=0
    end=len(array)-1
    middle=floor((start+end)/2)
    #print(start,middle,end)
    while not(array[middle]==value) and start<end:
        if value<array[middle]:
            end=middle-1
        else:
            start=middle+1
        middle=floor((start+end)//2)

    if array[middle]==value:
        return middle
    else:
        return -1


print(binarysearch(cs,90))


