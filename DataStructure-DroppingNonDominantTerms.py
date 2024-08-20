# we will drop the non dominant terms from the complexity that we have calculated.


def multiply(n):
    for i in range(n):      #----------------------------------------> The Time complexity is O(n)
        for j in range(n):  #----------------------------------------> The Time complexity is O(n)
            print(i,j)      #----------------------------------------> Total complexity of both loops is O(n^2) since both are nested loops.

    for k in range(n):#----------------------------------------> The Time complexity is O(n)
        print(k) #----------------------------------------> Total complexity is O(n)

multiply(10)


# Total complexity is O(n^2+n) . Out of which the dominant one is O(n^2) so we will discard O(n) as it is non dominant.
# so the required and the final complexity is O(n^2).