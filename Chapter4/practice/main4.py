data = ["3-A","2-B","1-C","3-D","1-E","3-F","1-G","2-H","3-I"]

for value in data:
    year , name = value.split("-")
    print(year,name)