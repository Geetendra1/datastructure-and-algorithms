def main(arr):
    n = len(arr)
    sum = 17
    curr_sum = 0
    start = 0
    for i in range(n):
        if i < n:
            curr_sum += arr[i]
        
        while(curr_sum > sum):
            curr_sum = curr_sum - arr[start]
            start += 1
        
        if curr_sum == sum:
            return 'True'
    return 'False'
           



if __name__ == "__main__":
    arr = [4,8,12,5]
    n = main(arr)
    print(n)