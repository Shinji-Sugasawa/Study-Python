my_pets = { 'dog','cat','dog'}
friend_pets = {"hamster",'cat'}

print(my_pets)#dogが重複しているため、出力は{'cat', 'dog'}

print(my_pets | friend_pets)#和集合 {'dog', 'hamster', 'cat'}

print(my_pets & friend_pets)#積集合 {'cat'}
