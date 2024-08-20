t1 = (1,2,3)
t2= (4,5,6)

def add_element(t1,t2):
    if len(t1)!=len(t2):
        return f'Input Tuples must have same length'
    else:
        result = tuple(a+b for a,b in zip(t1,t2))
        return result

print(add_element(t1,t2))