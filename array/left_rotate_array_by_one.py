def left_rotate_array_by_one(arr):
    temp = arr[0]
    for i in range(1,len(arr)):
        arr[i-1] = arr[i]
    
    arr[len(arr)-1] = temp
    return arr
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    n = left_rotate_array_by_one(arr)
    print(n)