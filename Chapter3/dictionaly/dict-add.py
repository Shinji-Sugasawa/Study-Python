user = {'name':'Shinji','age':21}

user['name'] = 'terada'
print(user['name'])#terada

user['tell'] = '123-4566-8901'
print(user)#{'name': 'terada', 'age': 21, 'tell': '123-4566-8901'}

print(int(user['age'])+1)#22 ←listは数値を入れてもstrで返される
print(user.get('age')+3)#get()メソッドを使えばintで返される