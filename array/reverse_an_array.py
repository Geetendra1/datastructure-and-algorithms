def reverse_an_array(arr):
    low = 0
    high = len(arr) - 1

    while low < high: 
        temp = arr[low]
        arr[low]  = arr[high]
        arr[high] = temp

        high -= 1
        low += 1
  
    return arr

if __name__ == "__main__":
    arr = [5, 8, 20, 21]
    print(reverse_an_array(arr))