def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def add_to_sub(a,b,c):
    added = add(a,b)
    return added - c

if __name__ == "__main__":
    print(add(1,2))
    print(add_to_sub(10,2,4))