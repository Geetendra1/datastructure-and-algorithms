
def frequency_in_sorted_array(arr):
    frequency = 1
    i = 1
    n = len(arr)
    while i < n:
        while (i < n and arr[i] == arr[i-1]):
            frequency += 1
            i += 1

        print(arr[i-1], '', frequency)
        i +=1
        frequency = 1

    if(n == 1 or arr[n-1] != arr[n-2]):
        print(arr[n-1],'',1)
    
if __name__ == "__main__":
    arr = [10,10,20,20,30]
    frequency_in_sorted_array(arr)


