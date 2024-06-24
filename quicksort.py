# def partition(arr,low,high):

#     pivot = arr[low]
#     i = low -1
#     j = i+1

#     while j<high:
#         if pivot<= arr[j]:
#             i += 1
#             arr[i],arr[j] = arr[j],arr[i]

#         j+=1
#     return i+1


# def quicksort(arr,low,high):
#     if low<high:

#         pivot_idx = partition(arr,low,high)
#         quicksort(arr,low,pivot_idx-1)
#         quicksort(arr,pivot_idx+1,high)
        

# a = [51,70,28,12,75,62,88,43]
# quicksort(a,0,len(a)-1)


def partition(arr, low, high):

    pivot = arr[high]
   

    i = low - 1
   

    for j in range(low, high):

        if arr[j] <= pivot:

            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1

def quicksort(arr, low, high):
    if low < high:

        pivot_index = partition(arr, low, high)
       

        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)


a = [51, 70, 28, 12, 75, 62, 88, 43]
quicksort(a, 0, len(a) - 1)

print(a)