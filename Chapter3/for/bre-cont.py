total = 0
for i in range(1,21):
    
    if i % 2 == 1: #奇数判定
        continue
    
    if i > 15:
        break
    
    total += i

print(total)