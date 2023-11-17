def move_array_at_last(arr):
    res = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            temp = arr[res]
            arr[res] = arr[i]
            arr[i] = temp
            res += 1
    return arr
if __name__ == "__main__":
    arr = [4,0,0,40,0,3,0]
    n = move_array_at_last(arr)
    print(n)