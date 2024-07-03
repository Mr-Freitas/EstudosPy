def exibir(n,j):
    if(n  == j): 
         print("Fim")
    else:
         print(n)
         return exibir(n +1,j)       

exibir(0,100)
    

        