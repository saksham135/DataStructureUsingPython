# Insert at the Beginning
# Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the beginning of the original tuple.
#
# Example
#
# input_tuple = (2, 3, 4)
# value_to_insert = 1
# output_tuple = insert_value_front(input_tuple, value_to_insert)
# print(output_tuple)  # Expected output: (1, 2, 3, 4)


existin_tuple = (1,2,3,4)
#
# def add_element(c_tuple,value):
#     n_l = []
#     n_l.append(value)
#     for i in c_tuple:
#         n_l.append(i)
#     n_t = tuple(n_l)
#     return n_t

def add_element(t1,value_to_inert):
    return (value_to_inert,)+t1

result = add_element(existin_tuple,55)
print(result)