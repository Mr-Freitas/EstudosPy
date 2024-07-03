from bisect import bisect_left

def BinarySearch(list,n):
    frist = 0
    last = len(list) -1
    
    while last >= frist:
        mid = (frist + last)//2
        if list[mid] == n:
            return True
        else:
            if n< list[mid]:
                last = mid - 1
            else:
                frist = mid + 1
    return False


list = [1,2,3,4,5,6,7,8,9,10]

print(BinarySearch(list,11))
print(bisect_left(list, 2))

def binary_Search(list,traget):
    index = bisect_left(list,traget)
    if index <= len(list) and list[index] == traget:
        return True
    return False


