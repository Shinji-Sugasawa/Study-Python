age = 20 
print("int → str")
#print("I\'m "+age+" old.") 変数 age が int 型のため実行不可
print("I\'m "+str(age)+" years old.")

age = "20"
print("str → int")
#print(age + 1) 変数 age が str 型のため実行不可
print(int(age)+1)