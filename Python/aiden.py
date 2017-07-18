num = int(input("choose number wisely "))
aiden = []
if(num == 11):
    print("wrong answer")
if (num != 11):
    x = 0
    while( x < num):
        y= 0
        while(y < num):
            aiden.append(",")
            y = y+1
        print(*aiden)
        aiden = []
        x = x+1
