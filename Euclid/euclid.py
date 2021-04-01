def gcd(x,y):   #ユークリッドを求める関数
    if y == 0:  #ｙの値が0ならば
        return x    #xの値を返す
    else:   #yの値が0以外ならば
        return gcd(y,x % y) #再起を用いる

get_x = input("1つ目の数値を代入してください:")#1つ目の数値をget_xに代入
get_y = input("2つ目の数値を代入してください:")#2つ目の数値をget_yに代入


print(gcd(int(get_x),int(get_y)))   #gcdを呼び出す