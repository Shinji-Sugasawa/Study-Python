user = {'name':'Shinji','age':21}

print(user.get('name'))#Shinji

print(user.get('hoge'))#None
print(user.get('hoge','番号なし'))#番号なし
