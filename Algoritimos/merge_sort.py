def MergeSort(list):
    if len(list) > 1:
        mid = len(list)//2
        left_half = list[:mid]
        right_half = list[mid:]
        MergeSort(left_half)
        MergeSort(right_half)
        
        left_ind = 0
        right_ind = 0
        alist_ind = 0 
        
        while left_ind < len(left_half) and right_ind < len(right_half):
            if left_half[left_ind] <= right_half[right_ind]:
                list[alist_ind] = left_half[left_ind]
                left_ind +=1 
            else:
                list[alist_ind] = right_half[right_ind]
                right_ind +=1
            alist_ind +=1 
            
            while left_ind < len(left_half):
                list[alist_ind]  = left_half[left_ind]
                left_ind += 1 
                alist_ind += 1
            
            while right_ind < len(right_half):
                list[alist_ind] = right_half[right_ind]
                right_ind += 1 
                alist_ind += 1 
            
    
                
                

list = [8,1,9,3]
MergeSort(list)