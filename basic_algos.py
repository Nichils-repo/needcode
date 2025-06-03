#bubble sort

def bubble_sort (arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        # if the algo does not swap even once in a single pass
        # then the array is already sorted
        #tracking the swap can help us avoid addition passes 

        for j in range(0, n- i -1):
            if arr[j] > arr [ j + 1]:
                # replace them 
                arr[j], arr[j+1] = arr[j+1], arr[j]

                swapped = True

        
        if not swapped:
            break
    
    return arr

