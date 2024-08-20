# + Operator : Concatenate List

# a=[1,2,3]
# b=[4,5,6]
# c=a+b
# print(c)

# * operator: Is used to repeate the elements of the list for the specific times
# a=[0,1]
# print(a*4)



# List Functions

# 1.len() Function :  # len fucntion count the total number of elements present in the list

# a=[1,2,3,4,5,6]
# print(len(a))

#2. Max() Function: Max Function returns the maximum value element from the list

# a=[10,70,65,43]
# print(max(a))


#3. min() Function: Min Function returns the element with the minimum value in the list

# a=[12,5,3,19]
# print(min(a))

#4. sum() Function: return the sum of all the element in the list
# a=[12,14,56,89]
# print(sum(a))

#5.Average() Function : returns the sum of all elements in the list divided by the total number of elements in the list
# a=[12,54,32,45]
# c=sum(a)/len(a)
# print(c)

# Method 1 : Finding Average using the list methods
# l1=[]
#
# while True:
#     inp=(input('Enter the values'))
#     if inp=='done':
#         break
#     else:
#         value = float(inp)
#         l1.append(value)
#
# average = sum(l1)/len(l1)
# print(f'Average is {average}')

total = 0
count = 0

while True:
    inp=(input("Enter the values"))
    if inp=='done':
        break
    else:
        value = float(inp)
        total = total+value
        count=count+1
        average=total/count

print('Average is ',average)