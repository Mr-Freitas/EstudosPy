def Busca(a_list):
    list =[]
    for i in a_list:
        if len(i) <= 4:
            list.append(i)
    return list
    
    
    
    




a_list = ["seltaught","code","sit","eat","programming","dinner","one","two","coding","a","tech"]

        
print(Busca(a_list))