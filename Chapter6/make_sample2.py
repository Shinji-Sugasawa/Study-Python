with open("sample2.txt","w",encoding ="utf-8") as f:
        f.write("私の名前は鈴木太郎です。\n")
        f.write("私の職業は、学生です。")


with open("D:\Documents\GitHub\Study-Python\Chapter6\sample2.txt","r",encoding = "utf-8") as f:
        print(f.read())
