# so we will insert new elements in form of rows and columns in the existing array .
# 1.insert method
# 2.append method

from numpy import *

#-------------------------------------------------------1.insert method ------------------------------------------------

#syntax-insert(array_name,index,Elements,axis=0 or 1 [0 for Rows and 1 for Column Addition])


################################################################Case1################################################################
#Insertion of Columns

two_array = array([[10,20,30,40],[50,60,70,80],[90,100,110,120],[130,140,150,160] ])

# n_array=insert(two_array,0,[230,240,260,550],axis=0)

# n_array=insert(two_array,2,[230,240,260,550],axis=0)


################################################################Case2################################################################
#Insertion of Columns

# n_array = insert(two_array,1,[111,222,333,444],axis=1)
#
# print(n_array)


#Time Complexity for addding the new Rows and the Columns in the existing array is O(mn)
#where m is the number of columns and n is the number of rows.


#-------------------------------------------------------2.append method ------------------------------------------------

################################################################Case1################################################################
#Insertion of Columns

n_array = append(two_array,[[110,220,320,440]],axis=0)
print(n_array)