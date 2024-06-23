import time
start = time.perf_counter()
a = [9,11,15,21,23,25,29,30,35]




# def binary_search(arr,n):
#     if len(arr)>=1 and arr[0]<= n <= arr[len(arr)-1]:
#         mid = len(arr)//2
#         if n == arr[mid]:
#             return f"Your searching value {arr[mid]} is present in the array"
#         elif n > arr[mid]:
#           return binary_search(arr[mid+1:],n)
#         # elif n < arr[mid]:
#         else:
#             return binary_search(arr[:mid],n)
#     else:
#         return f"Unfortunately {n} is not in the array"
        



# searching_for = binary(a,31)
# print(searching_for)


def ternary_search(arr,n):
    if len(arr)>=1 and arr[0]<= n <= arr[len(arr)-1]:

        mid1 = len(arr)//3
        mid2 = len(arr)-mid1
        if n == arr[mid1] or n == arr[mid2]:
            return f"Your searching value {n} is present in the array"       
        elif arr[mid1] < n < arr[mid2]:
          return ternary_search(arr[mid1+1:mid2],n)
        elif n > arr[mid2]:
          return ternary_search(arr[mid2:],n)
        else:
            return ternary_search(arr[:mid1],n)
    else:
        return f"Unfortunately {n} is not in the array"
    

searching_for = ternary_search(a,31)
print(searching_for)
end = time.perf_counter()
print("execution time",end - start)