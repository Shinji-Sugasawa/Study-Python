def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x % y)

get_x = input("1つ目の数値を代入してください:")#1つ目の数値をget_xに代入
get_y = input("2つ目の数値を代入してください:")#2つ目の数値をget_yに代入

print(gcd(get_x,get_y))