
##############################################################Update Operaton##################################################
my_list = [1,2,3,4,5,6]
print(my_list)

# my_list[2]=33
# print(my_list)
#
# my_list[4]=55
# print(my_list)


#Time Complexity of Update Operation is O(1)
# Space Complexity of Update Operation is O(1).

#Insertion Operation

#1.Insertion at the Beginning of the List.
#2.Insertion at the any given place .
#3.Insertion at the end of the List .
#4.Inserting a new List in the existing List.


#List Methods : We will use the following list methods :
# 1.insert()
# 2.append()
# 3.extend()


#Case1-Using the Insertion Method
#At Beginning:
# print('Before Insertion')
# my_list.insert(0,11)
# print('After Insertion')
# print(my_list)

#Time complexity for Insertion at Beginning is O(1)
# Space Complexity for Insertion at Beginning is O(1)

# At Middle:
print('Before Insertion')
# my_list.insert(4,55)
# print('After Insertion')
# print(my_list)

#Time complexity for insertion at middle is O(n) as we have to shift the elements towards the left .
#Space complexity for insertion at middle is O(1).


#Case -2 Using the append method we will insert at the last .

# my_list.append(60)
# print(my_list)

# Time complexity for insertion at end using the append method is O(1)
# Space complexity for insertion at end using the append method is O(1).

#Case -3 Using the extend method

n_l = [50,60,70,80,90]
my_list.extend(n_l)
print(my_list)

#Time complexity for the extend method is the total number of elements = O(n)
# Space complexity is O(n) also depend on number of elements.

