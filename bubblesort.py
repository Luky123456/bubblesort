def bubble(list):
    for i in range (0,len(list)):
        for y in range (0,len(list)-i-1):
            if list[y]>list[y+1]:
                list[y],list[y+1]=list[y+1],list[y]
                print(list)
    return list

print(bubble([2,5,6,1,2]))