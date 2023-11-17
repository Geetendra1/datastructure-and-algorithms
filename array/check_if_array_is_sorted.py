def check_if_array_is_sorted(arr):
    
    for i in range(1,len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

if __name__ == "__main__":
    arr = [5, 8, 12, 2,2]
    print(check_if_array_is_sorted(arr))


