# The Cube Complexity is the thrice the original complexity .

def multiply(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)

multiply(10)

# The Above code will run for the 1000 times for the given input .
#The above code is the example of the Cube time complexity since
# above code run for 1000 times since it has already  two loops and we added one more
# extra loop inside it which can be also called nested loop. 