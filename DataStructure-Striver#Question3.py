def nextPermutation(A) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = len(A)-2
    while i>=0 and A[i]>A[i+1]:
        i-=1
    if i>=0:
        j = len(A)-1
        while j>=0 and A[j] <=A[i]:
            j-=1
        A[i],A[j]=A[j],A[i]
    A[i+1:]=reversed(A[i+1:])
    return A

if __name__ == "__main__":
    A = [2, 1, 5, 4, 3, 0, 0]
    ans = nextPermutation(A)
    print(ans)
    # print("The next permutation is: [", end="")
    # for it in ans:
    #     print(it, end=" ")
    # print("]")