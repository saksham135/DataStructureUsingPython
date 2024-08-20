                                                # Sorting Algorithms

from math import *

cs = [2,1,7,6,8,9,5,4,3]

# Type-1-Bubble sort

# def bubblesort(customlist):
#     for i in range(len(customlist)):
#         for j in range(len(customlist)-i-1):
#             if customlist[j]>customlist[j+1]:
#                 customlist[j],customlist[j+1]=customlist[j+],customlist[j]
#     print(customlist)
#
# bubblesort(cs)

# Type-2-Selection Sort

# def selectionsort(customlist):
#     for i in range(len(customlist)):
#         min = i
#         for j in range(i+1,len(customlist)):
#             if customlist[min]>customlist[j]:
#                 min = j
#         customlist[i],customlist[min]=customlist[min],customlist[i]
#     print(customlist)
#
#
# selectionsort(cs)


# Type-3 Insertion sort

# def insertionsort(customlist):
#     for i in range(1,len(customlist)):
#         key = customlist[i]
#         j = i-1
#         while j>=0 and key<customlist[j]:
#             customlist[j+1]=customlist[j]
#             j-=1
#         customlist[j+1]=key
#     return insertionsort

# Type-4 Bucket sort
# def bucketsort(customList):
#     numberofBuckets = round(sqrt(len(customList)))
#     maxValue = max(customList)
#     arr = []
#
#     for i in range(numberofBuckets):
#         arr.append([])
#     for j in customList:
#         index_b = ceil(j * numberofBuckets / maxValue)
#         arr[index_b - 1].append(j)
#
#     for i in range(numberofBuckets):
#         arr[i] = insertionsort(arr[i])
#
#     k = 0
#     for i in range(numberofBuckets):
#         for j in range(len(arr[i])):
#             customList[k] = arr[i][j]
#             k += 1
#     return customList



# bucketsort(cs)

# Type-5 Merge sort

# def merge(customList, l, m, r):
#     n1 = m - l + 1
#     n2 = r - m
#
#     L = [0] * (n1)
#     R = [0] * (n2)
#
#     for i in range(0, n1):
#         L[i] = customList[l + i]
#
#     for j in range(0, n2):
#         R[j] = customList[m + 1 + j]
#
#     i = 0
#     j = 0
#     k = l
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             customList[k] = L[i]
#             i += 1
#         else:
#             customList[k] = R[j]
#             j += 1
#         k += 1
#     while i < n1:
#         customList[k] = L[i]
#         i += 1
#         k += 1
#
#     while j < n2:
#         customList[k] = R[j]
#         j += 1
#         k += 1
#
# def mergesort(customlist,l,r):
#     if l<r:
#         m=(l+(r-1))//2
#         mergesort(customlist,l,m)
#         mergesort(customlist,m+1,r)
#         merge(customlist,l,m,r)
#     return customlist
#
#
#
# print(mergesort(cs,0,8))
#


# Type-6 Quick Sort

# def swap(my_list,index_1,index_2):
#     my_list[index_1],my_list[index_2]=my_list[index_2],my_list[index_1]
#
# def pivot(my_list,pivot_index,end_index):
#     swap_index = pivot_index
#     for i in range(pivot_index+1,end_index+1):
#         if my_list[i]<my_list[pivot_index]:
#             swap_index+=1
#             swap(my_list,swap_index,i)
#     swap(my_list,pivot_index,swap_index)
#     return swap_index
#
# def quicksort_helper(my_list,left,right):
#     if left<right:
#         pivot_index = pivot(my_list,left,right)
#         quicksort_helper(my_list,left,pivot_index-1)
#         quicksort_helper(my_list,pivot_index+1,right)
#     return my_list
#
# def quicksort(my_list):
#     return quicksort_helper(my_list,0,(len(my_list))-1)
#
#
# my_list = [3,5,0,6,2,1,4]
# print(quicksort(my_list))

# Type-7 Heap Sort
def heapify(customlist,n,i):
    smallest = i
    l = 2*i+1
    r = 2*i+2
    if l<n and customlist[l]<customlist[smallest]:
        smallest = l

    if r<n and customlist[r]<customlist[smallest]:
        smallest = r

    if smallest!=i:
        customlist[i],customlist[smallest]=customlist[smallest],customlist[i]
        heapify(customlist,n,smallest)


def heapsort(customlist):
    n=len(customlist)
    for i in range(int(n/2),-1,-1):
        heapify(customlist,n,i)

    for i in range(n-1,0,-1):
        customlist[i],customlist[0]=customlist[0],customlist[i]
        heapify(customlist,i,0)
    customlist.reverse()


heapsort(cs)
print(cs)







