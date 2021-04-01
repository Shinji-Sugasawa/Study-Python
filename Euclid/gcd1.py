def gcd(x,y):
    x_list = []
    y_list = []
    
    count = 1
    while x > count:
        if count % x == 0:
            x_list.append(count)
        count +=1
    
    count = 1
    while y > count:
        if count % y == 0:
            y_list.append(count)
        count +=1
        
    count_x,count_y = 0,0
    gcd_list = []
    for count_x in list_x:
        for count_y in y_list:
            if cont_x == count_y:
                gcd_list.append(count_x)
    
    return max(gcd_list)

print(gcd(12,18))