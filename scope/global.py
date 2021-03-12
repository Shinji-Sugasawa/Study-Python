initial = 20

def add(a,b):
    global initial #グローバルスコープを書き換え
    initial = a + b
    return initial

print (initial) # --> 20
print (add(1,2)) # --> 3
print (initial) # --> 3 
