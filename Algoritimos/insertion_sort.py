def insertioSort(list):
    for i in range(1,len(list)):
        value = list[i]
        while i > 0 and list[i-1] > value:
            list[i] = list[i-1]
            i = i-1
        list[i] = value
    return list

list=[54,78,9,1]

print(insertioSort(list))