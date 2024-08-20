# for storing integer numbers

# def mod(number,cell_number):
#     return number%cell_number
#
#
# print(mod(300,24))


# for storing string

def modascii(string,cel_number):
    total = 0
    for i in string:
        total+=ord(i)
    return total%cel_number

print(modascii('Hello',24))