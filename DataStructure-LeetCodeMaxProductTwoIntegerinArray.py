#Given the array of integers nums, you will choose two different indices
# i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1)

choice = (int(input('How Many Number of Elements you want to input in array?')))
my_array = []

for i in range(choice):
    print(f'Enter Element {i+1} to be inserted at index {i}')
    add_me=(int(input()))
    my_array.append(add_me)

print('The Elements in List are:',my_array)

def max_arr_integer(arr):
    new_list = []
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            new_list.append((arr[i]-1)*(arr[j]-1))
    return max(new_list)

result = max_arr_integer(my_array)
print('Maximum of two inetgers in array are:',result)