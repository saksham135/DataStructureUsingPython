# Common Elements
# Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.

# Example

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

def common_elements(tuple1,tuple2):
    # n_l = []
    # for i in range(len(tuple1)):
    #     for j in range(len(tuple2)):
    #         if tuple1[i]==tuple2[j]:
    #             n_l.append(tuple1[i])
    #             n_l.append(tuple2[j])
    # n_l = set(n_l)
    # n_l = tuple(n_l)
    # return n_l
    return tuple(set(tuple1)&set(tuple2))

output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)  # Expected output: (4, 5)