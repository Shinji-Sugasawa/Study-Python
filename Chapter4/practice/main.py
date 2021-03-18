text = "I am learning Pyton programming language"

split_text = text.split(" ")
#単語をスペースで分割
print(split_text)
#分割結果を出力

counter = 0
for word in split_text:#forループで分割した文字列を処理
    if len(word) >= 3:
        counter += 1 #文字をカウント

print(f"単語の数:{counter}")#画面に出力する