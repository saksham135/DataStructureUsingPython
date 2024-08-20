# so for two dimensional Array we will use numpy array module for creating the two dimensional array .

# so reason for two dimensional array use is that sometime we are
# given data with multiple columns and rows that the 1d array cannot handle and that's why we need the numpy module

# example -  Day1=[10,20,30,40],
#            Day2=[50,60,70,80],
#            Day2=[90,100,110,120],
#            Day2=[130,140,150,160],

from numpy import *


two_array = array([[10,20,30,40],[50,60,70,80],[90,100,110,120],[130,140,150,160] ])

print(two_array)


#Time Complexity for creating the 2D Array is O(m)(n) where m is the total number of rows and n is the total number of columns.
