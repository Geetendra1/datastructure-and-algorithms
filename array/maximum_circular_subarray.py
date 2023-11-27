def main(arr):
    res = arr[0]
    for i in range(len(arr)):
        curr_sum = arr[i]
        curr_max = arr[i]
        for j in range(1,len(arr)):
            index = (i+j)% len(arr)
            curr_sum = curr_sum + arr[index]
            curr_max = max(curr_max,curr_sum)
        res = max(curr_max,res)
    return res



if __name__ == "__main__":
    arr = [-3,8,-2,4 -5,6]
    n = main(arr)
    print(n)