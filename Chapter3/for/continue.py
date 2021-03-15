total = 0
for number in[1,3,10]:
    print(number)
    continue
    total += number #ここは実行されない

print('totalの値'+str(total))