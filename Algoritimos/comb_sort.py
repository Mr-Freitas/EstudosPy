def comb_sort(arr):
    def get_next_gap(gap):
        gap = (gap * 10) // 13  # Redução do gap por um fator de 1.3
        if gap < 1:
            return 1
        else:
            return gap
    
    n = len(arr)
    gap = n  # Inicializa o gap com o tamanho da lista
    swapped = True  # Flag para verificar se houve trocas
    
    while gap != 1 or swapped:
        gap = get_next_gap(gap)
        swapped = False
        
        # Comparação e troca dos elementos com o gap atual
        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
    
    return arr

# Exemplo de uso:
arr = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", arr)
sorted_arr = comb_sort(arr)
print("Lista ordenada:", sorted_arr)
