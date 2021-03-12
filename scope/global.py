initial = 20

def add(a,b):
    global initial
    initial = a + b
    return initial

print (initial) # --> 23 
print (add(1,2)) # --> 3
print (initial) # --> 3 
