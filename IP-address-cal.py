address = 2
print("アドレスのビット数は何ビット?")
bit = input()

for i in range(0,int(bit)-1):
    address *= 2

print("アドレス数 : "+str(address))