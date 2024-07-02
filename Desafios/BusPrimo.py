def buscarP(n):
    num = []
    if n !=0:
        for i in range(2,n):
            if i % 2 == 1:
                num.append(i)
        print(num)
    return False


buscarP(57)