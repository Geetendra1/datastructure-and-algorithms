def get_second_largest(arr):
    largest = 0
    second = -1
    for i in range(len(arr)):
        if arr[i] > arr[largest]:
            second = largest
            largest = i
        
        elif (arr[i] != largest | arr[i] > arr[second] ):
            second = i

            
    return arr[second]


if __name__ == "__main__":
    arr = [5, 8, 20, 22, 21]
    print(get_second_largest(arr))