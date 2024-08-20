my_numbers = (int(input('Enter the total number of elements to be entered in list.')))
my_list = []

for j in range(my_numbers):
    print(f'Element at index {j}:')
    value = (int(input(f'Enter the Element{j+1}')))
    my_list.append(value)
print('List after inputting inputs is:',my_list)

def find_pair(list1,target):
    n_l=[]
    for i in range(0,len(list1)):
        for k in range(i+1,len(list1)):
            if list1[i]+list1[k]==target:
                n_l.append(list1[i])
                n_l.append(list1[k])
    print('The Pair is:',n_l)

target=(int(input('Enter the target element')))
find_pair(my_list,target)