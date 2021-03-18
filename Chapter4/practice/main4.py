data = ["3-A","2-B","1-C","3-D","1-E","3-F","1-G","2-H","3-I"]

counter = {}

for value in data:
    year , name = value.split("-")
    
    if year not in counter:
        counter[year] = []
    
    counter[year].append(name)
    
for year in sorted(counter):
#counterという辞書のキーをsorted関数でソートする
#１つずつ取り出す
    print(f"{year}年")
    for order , name in enumerate(counter[year]):
#enumerateはインデックス番号、要素の順で取得される
#orderにindex値、nameにyearキーの要素を代入
        print(f"{order+1}位 : {name}")
    print()