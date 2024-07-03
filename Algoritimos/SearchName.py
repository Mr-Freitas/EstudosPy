from bisect import bisect_left

def SearchName(list,name):
    index = bisect_left(list,name)
    if index >= len(list):
        return False
    
    elif index <= len(list) and list[index] == name:
        return True
    
    

list = ['ANA','BETO','CAIO']

print(SearchName(list,'ANA'))