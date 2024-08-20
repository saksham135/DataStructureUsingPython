def linearsearch(customlist,value):
    for i in range(len(customlist)):
        if customlist[i]==value:
            return i
    return -1


cs=[20,40,30,90,32]
print(linearsearch(cs,90))