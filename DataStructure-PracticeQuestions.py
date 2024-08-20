# Question-1
# How do you reverse a string?
# Reversing a string is a common coding task. Achieve this by looping through the string’s characters and constructing a reversed string.

# Method -1 :  using string concatenation 

# inp =(input('Enter the string you want to reverse'))

# using slicing
# print(inp[::-1])

# Method-2
# using for loop
# str=""
# for i in inp:
#     str=i+str
# print(str)

# Method-3
# using recursion 

# reversing a python string using stack 
# class Node:
#     def __init__(self,value):
#         self.value = value 
#         self.next = None 
    
# class LL:
#     def __init__(self):
#         self.head = None 
        
#     def __iter__(self):
#         current = self.head 
#         while current:
#             yield current
#             current = current.next
    
# class Stack:
#     def __init__(self):
#         self.LL= LL()
        
#     def __str__(self):
#          values = [str(x.value) for x in self.LL]
#          return '\n'.join(values)
        
#     def isempty(self):
#         if self.LL.head==None:
#             return 'No Element in the stack'
#         else:
#             return 'Stack is not Empty'
        
#     def push(self,value):
#         node = Node(value)
#         node.next = self.LL.head
#         self.LL.head = node 
            
#     def pop(self):
#         if self.isempty():
#             return "There is not any element in the stack"
#         else:
#             nodeValue = self.LinkedList.head.value
#             self.LinkedList.head = self.LinkedList.head.next
#             return nodeValue
        

# c = Stack()
# c.push('H')
# c.push('E')
# c.push('L')
# c.push('L')
# c.push('O')
# print(c)

# How to check whether a string is palindrome or not
# my_str=''
# for i in inp:
#     my_str=i+my_str
# if my_str==inp:
#     print('Yes Palindrome string')
# else:
#     print('No')

# class Node:
#     def __init__(self,value):
#         self.value = value 
#         self.next = None 
    
# class LL:
#     def __init__(self):
#         self.head = None 
    
#     def __str__(self):
#         values = [str(x) for x in self.LL]
#         return '\n'.join(values)
        
#     def __iter__(self):
#         current = self.head 
#         while current:
#             yield current 
#             current = current.next
            
# class Stack:
#     def __init__(self):
#         self.LL = LL()
        
#     def isempty(self):
#         if self.head == None:
#             return 'Stack is empty'
#         else:
#             return 'stack has elements'
    
#     def push(self,value):
#         node = Node(value)
#         node.next = self.LL.head 
#         self.LL.head = node 
        
#     def pop(self):
#         if self.isempty():
#             return 'Stack is Empty'
#         else:

            
# swiping program 

# num1 = (int(input('Enter Number1')))
# num2 = (int(input('Enter Number2')))

# def swipe(n1,n2):
#     t = n1 
#     n1=n2 
#     n2=t 
#     return n1,n2 

# print(swipe(num1,num2))

# a= [1,2,5,3,4,6,7,8]
#
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]>a[i+1]:
#             # a[i],a[j]=a[j],a[i]
#             temp = i
#             i= j
#             j = temp
#
#
# print(a)

# a= [1,2,5,3,4,6,7,8]
#
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
#
# print('The List in discending order is',a)
#
# def find_second(arr):
#     for i in range(len(arr)):
#         if arr[i]!=arr[0]:
#             return arr[i]
#
#
# print(find_second(a))

# def find_prime(n):
#     for i in range(2,n+1):
#         for j in range(2,n+1):
#             if i%j==0:
#                 break
#
#         if i==j:
#             print(i,end=' ')
#
#
# find_prime(101)



# i = 2
#
# while i <= 100:
#     j = 2
#     while j < 100:
#         if i%j == 0:
#             break
#         j += 1
#     if i == j:
#         print(i,end=',')
#     i += 1

# def reverse_s(stri):
#     if len(stri)==0:
#         return None
#     elif len(stri)<=1:
#         return stri
#
#     else:
#         return stri[-1]+reverse_s(stri[:-1])
#
# print(reverse_s('Hello'))

# def rever_s(s):
#     t = ''
#     for i in range(len(s)):
#         t=s[i]+t
#     return t
#
# print(rever_s('Hello'))
# import numpy as np
# integer_array = np.random.randint(0, 10, (3,3))
# integer_array2 = np.random.randint(0,20,(3,3))
# zeroes = np.zeros((3,3))
#
# print(integer_array)
# print(integer_array2)
# print(zeroes)
#
# print('After Addition')
# for i in range(len(integer_array)):
#     for j in range(len(integer_array2)):
#         zeroes[i][j]=integer_array[i][j]+integer_array2[i][j]
#
# print(zeroes)

# stri = "Welcome to TutorialsPoint family";
# print("All the duplicate characters in the string are: ");
#
# for i in range(0,len(stri)):
#     count =1
#     for j in range(i+1,len(stri)):
#         if stri[i]==stri[j] and stri[i] != ' ':
#             count = count+1
#
#     stri=stri[:j]+'0'+stri[j+1:]
#
#     if (count>1 and stri[i]!='0'):
#         print(stri[i],'-',count)


# str1 = 'abcdef'
# str2 = 'defghia'

# def count(str1,str2):
#     match_count = 0
#     same_char = []
#     for i in range(0,len(str1)):
#         if str1[i] in str2:
#             match_count+=1
#             same_char.append(str1[i])
#     return match_count,same_char
#
# print(count(str1,str2))



# str1 = (input('Enter string'))
# vowels = ['a','e','i','o','u']
#
# def find_vowels(str1):
#     vow_count = 0
#     v_l=[]
#     for i in range(0,len(str1)):
#         if str1[i] in vowels:
#             v_l.append(str1[i])
#     v_l=set(v_l)
#     return f'The vowel count in string is{len(v_l)} and vowels are {v_l}'
#
#
# print(find_vowels(str1))

# num = (int(input('Enter the number')))
# count = 0
#
# for i in range(1,num+1,1):
#     if num%i==0:
#         count+=1
#         print('Factors are:',i)
# print('Total Number of Factors are',count)

# def find_fab(n):
#     a=0
#     b=1
#     if n<0:
#         print('Incomplete Input')
#     elif n==0:
#         return a
#     elif n==1:
#         return b
#     else:
#         for i in range(2,n+1):
#             c=a+b
#             a=b
#             b=c
#         return b
#
# def find_fab1(n):
#     if n in [0,1]:
#         return n
#     else:
#         return find_fab1(n-1)+find_fab1(n-2)
#
# print(find_fab(10))
# print(find_fab1(10))


# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length=0
#
#     def __str__(self):
#         temp = self.head
#         result =''
#         while temp:
#             result+=str(temp.value)
#             if temp is not None:
#                 result+='->'
#             temp = temp.next
#         return result
#
#     def append(self,value):
#         new_node = Node(value)
#         if self.length==0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length+=1
#
#     def prepend(self,value):
#         new_node = Node(value)
#         if self.length==0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.length+=1
#
#     def insert(self, index, value):
#         new_node = Node(value)
#         if index < 0 or index > self.length:
#             return False
#         elif index == 0:
#             new_node.next = self.head
#             self.head = new_node
#         elif self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             temp = self.head
#             for _ in range(index - 1):
#                 temp = temp.next
#             new_node.next = temp.next
#             temp.next = new_node
#         self.length += 1
#
#     def get(self,index):
#         if index==0:
#             return self.head.value
#         elif index==self.length-1:
#             return self.tail.value
#         elif index<0 or index>self.length:
#             return None
#         else:
#             temp = self.head
#             for _ in range(index):
#                 temp=temp.next
#             return temp.value
#
#     def search(self,value):
#         current = self.head
#         while current:
#             if current.value==value:
#                 return True
#             current=current.next
#         return False
#
#
#
# l = LinkedList()
# l.append(10)
# l.append(20)
# l.prepend(5)
# l.prepend(0)
# l.insert(3,15)
# print(l.search(10))

# import re 

# def removeuppercase(stri):
#     regex="[A-Z]"
    
#     return (re.sub(regex,"",stri))

# def removelowercase(stri):
#     regex="[a-z]"
#     return (re.sub(regex,"",stri))

# def removespecialcharacters(stri):
#     regex="[^A-Za-z0-9]"
#     return (re.sub(regex,"",stri))

# def removenumerical(stri):
#     regex="[0-9]"
    
#     return (re.sub(regex,'',stri))

# def removenonumeric(stri):
#     regex="[^0-9]"
    
#     return (re.sub(regex,'',stri))

# stri = "GFGgfg123$%"
# print("After removing uppercase characters:",
# removeuppercase(stri))
# print("After removing Lower characters:",
# removelowercase(stri))
# print("After removing special characters:",
# removespecialcharacters(stri))
# print("After removing uppercase characters:",
# removenumerical(stri))
# print("After removing uppercase characters:",
# removenonumeric(stri))



# Missing and Repeating 


# def printmissnumber(arr):
#     n = len(arr)
#     temp =[0]*n 
#     repeatednumber=-1 
#     missingnumber=-1 
    
#     for i in range(n):
#        temp[arr[i]-1]+=1
#        if temp[arr[i]-1]>1:
#            repeatednumber =arr[i]
    
#     for i in range(n):
#         if temp[i]==0:
#             missingnumber=i+1
#             break 
    
#     print('The Rpeating Number is',repeatednumber)
#     print('The Missing Number is',missingnumber)
    
# arr = [7, 3, 4, 5, 5, 6, 2]
# printmissnumber(arr)
        



# # How to find all permutations of String?
# def tostring(List):
#     return ''.join(List)


# def permuate(s,l,r):
#     if l==r:
#         print(tostring(s))
#     else:
#         for i in range(l,r):
#             s[l],s[i]=s[i],s[l]
#             permuate(s,l+1,r)
#             s[l],s[i]=s[i],s[l] # Backtrack 
            
            

# string = "ABC"
# n = len(string)
# a = list(string)

# permuate(a,0,n)
            
            

# # How to check if a given number is a Palindrome?
# number =(int(input('Enter the Number')))

# temp = number 
# rev = 0
# while(number>0):
#     dig = number%10 
#     rev = rev*10+dig 
#     number = number//10 
    
# if (temp==rev):
#     print('The Number is Palindrome')
# else:
#     print('The Number is not a palindrome')        
        
    
# # Program for average of an array (Iterative and Recursive)

# n = [1,2,3,4,5]


# def cal_average(arr):
#     n = len(arr)
#     sum = 0
#     for i in arr:
#         sum+=i
#     print('The average of array is',sum/n)
    
# cal_average(n)
    
    
# Write a Program to check if a given year is a leap year.

# year = (int(input('Enter the year to check whether it is leap year or not')))


# def check_leap(year):
#     if year%400==0 and year%100==0:
#         print(f'{year} is leap year')
#     elif year%4==0 and year%100!=0:
#         print(f'{year} is leap year')
#     else:
#         print(f'{year} is not a leap year')
    
# check_leap(year)

# write a program to check whether a number is palindrome or not 

# num  =(int(input('Enter the number to check whether a number is palindrome or not')))

# def check_palindrom(number):
#     temp = number 
#     rev = 0
#     while (number>0):
#         dig = number%10 
#         rev = rev*10+dig 
#         number = number//10 
        
#     if temp==rev:
#         print('The Number is palindrome')
#     else:
#         print('The number is not palindrome')
        
        
# check_palindrom(num)
num = (input('Enter Number'))
m=int(num)


    
        