def selection_sort(arr, stages=False):
    a = [arr[:]]    # List to store the intermediary stages of the main list arr after a swap takes place in arr
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the current minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
        if stages:
            # Append a copy of the itermediary list to the bigger list which will be returned later
            a.append(arr[:])    
    return a if stages else arr 


def bubble_sort(arr, stages=False):
    a = [arr[:]]
    n = len(arr)
    for i in range(n - 1):
        # Flag to detect whether at least one swap does take place
        swapped = False
        # Traverse the array till n-i-1 since the last i elements are already sorted after each iteration
        for j in range(0, n-i-1):
            # Swap if the current element is larger than the next one
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                a.append(arr[:])
                swapped = True    # Update flag
        # If no two elements were swapped in the inner loop, break
        # This is a non-mandatory piece of optimization code that breaks the loop since if no swaps have taken place, 
        # it means the list is sorted, despite the fact that there may be more elements to iterate over
        if not swapped:
            break
    return a if stages else arr


def insertion_sort(arr, stages=False):
    a = [arr[:]]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            a.append(arr[:])
            j -= 1
        arr[j + 1] = key
        a.append(arr[:])
    return a if stages else arr