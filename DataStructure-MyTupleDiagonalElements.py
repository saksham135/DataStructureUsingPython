# Diagonal
# Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.
#
# Example

input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

def get_diagonal(input_tuple):
    n_t = []
    for i in range(len(input_tuple)):
        n_t.append(input_tuple[i][i])
    return tuple(n_t)
output_tuple = get_diagonal(input_tuple)
print(output_tuple)  # Expected output: (1, 5, 9)