# Input the number of days
# inp = (int(input('Enter the Total Number of Days for temprature Check')))
# l1 = []
#
# for i in range(inp):
#     print(f'Temperature for day{i} is:')
#     day_temp = float(input('Enter Temperature?'))
#     l1.append(day_temp)
#
# average = sum(l1)/len(l1)
# print('Average of all Temperatures is :',average)
#
# for j in range(len(l1)):
#     if average>l1[j]:
#         print(f"Day {j}'s temperature is average.")

def temp_check(n):
    l2=[]
    for f in range(n):
        print(f'Temperature for day{f} is:')
        day_temp = float(input('Enter Temperature?'))
        l2.append(day_temp)
    average_temp = sum(l2)/len(l2)
    print(f'Average Temperature is {average_temp}')
    for s in range(len(l2)):
        if average_temp>l2[s]:
            print(f'Average Temperature for day {s} is average')

day_input = (int(input('Enter the total number of days for which input needs to be checked?')))
temp_check(day_input)