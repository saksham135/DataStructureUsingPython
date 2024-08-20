prev_list = [1,2,3,4]

#syntax : [new_item for item in list]

# new_list = [i**2 for i in prev_list]
# print(new_list)

# language = 'python'
#
# new_list = [ letter for letter in language]
# print(new_list)

list1 = [-1,20,-20,2,-90,60,45,20]

#
# new_list = [number for number in list1 if(number>0)]
# new_list = [number for number in list1 if (number**2)<0]
new_list = [number*number for number in list1 if number<0]
print(new_list)