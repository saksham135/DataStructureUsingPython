# Quadratic Time Complexity is the twice of the original complexity .


def multiply(n):
    for i in range(n):
        for j in range(n):
            print(i,j)


multiply(10)

#The above code is the example of the Quadratic time complexity since
# above code run for 100 times since it has already one loop and we added one more
# extra loop inside it which can be also called nested loop. If we add one more loop it will become the cube type complexity.