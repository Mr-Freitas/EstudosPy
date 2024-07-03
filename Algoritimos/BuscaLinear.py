def LinearSearch(list,n):
     for i in list:
         if i == n:
             return True
     return False
 
 
 
list =[1,2,3,4,5,6,7]
print(LinearSearch(list,45))


# print(1 in list)