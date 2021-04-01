def gcd(x,y):
    x_list = []
    y_list = []
    
    count = 1
    while x > count:
        if count % x == 0:
            x_list.append(count)
        count +=1
    
    count = 1