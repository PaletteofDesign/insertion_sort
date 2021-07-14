arr = [3,1,5,6,8,7,9,4,10,2]

def insertSort(arr):
    for i in range(len(arr)):
        c_val = arr[i]
        c_p = i

        while c_p > 0 and arr[c_p-1] > c_val:
            arr[c_p] = arr[c_p-1]
            c_p = c_p-1

        arr[c_p] = c_val

    return arr
    
print(insertSort(arr))
