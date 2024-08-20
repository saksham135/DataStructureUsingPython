def find_fac(n):
    assert n>=0 and int(n)==n,'The Number must be +ve integer only'
    if n in [0,1]:
        return 1
    else:
        return n*find_fac(n-1)


print(find_fac(6))