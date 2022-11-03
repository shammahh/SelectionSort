def selectionsort(arr):
    for fillslot in range(len(arr)):
        min = fillslot
        for i in range(min + 1, len(arr)):
            if  arr[i] < arr[min]:
                min = i
        get = (arr[fillslot], arr[min])
        (arr[min], arr[fillslot]) = get
    return(arr)
         
        

nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
###      0   1   2   3   4    5   6   7   8

print(selectionsort(nums))