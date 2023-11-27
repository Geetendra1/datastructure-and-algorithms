def main(arr):
    k = 3
    n = len(arr)
    curr_sum = 0
    curr_max = 0
    for i in range(k):
       curr_sum = curr_sum + arr[i]
    
    for i in range(k,n):
        curr_sum = curr_sum +( arr[i] - arr[i-k])
        curr_max = max(curr_max,curr_sum)
    print( curr_max)


if __name__ == "__main__":
    arr = [1,8,30,-5,20,7]
    n = main(arr)
    print(n)