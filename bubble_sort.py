def bubbleSort(list):
    listLength = len(list) -1
    for i in range (listLength):
        no_swaps = False
        for j in range(listLength):
            if list[j] > list[j +1 ]:
                list[j], list[j+1] = list[j+1],list[j]
                no_swaps = True
        if no_swaps:    
            return list

list=[34,6,20,56,1]

print(bubbleSort(list))