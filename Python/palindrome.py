palin = [
    ]
def fun():
    list1 = []
    for wange in range(100,1000):
        list1.append(wange)
        #print (list1)
    return list1
list_keeper = fun()
palindromemulitplier = 100
while(palindromemulitplier != 1000):
    i=0
    while(i != 899):
        palindromechecker = palindromemulitplier * list_keeper[i]
        palindromechecker = str(palindromechecker)
        if(palindromechecker == palindromechecker[::-1]):
            palindromechecker = int(palindromechecker)
            palin.append(palindromechecker)
        i = i + 1
    palindromemulitplier = palindromemulitplier + 1
aiden = max(palin)
print(aiden)
