initial = 20

def add(a,b):
    initial = a + b
    return initial

print (add(1,2))    # --> 3
print (initial) # --> 20 
#関数内に同じ名前のローカルスコープ変数があるが、グローバルスコープの変数を上書きしない