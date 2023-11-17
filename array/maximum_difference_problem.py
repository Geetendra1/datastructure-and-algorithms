
def maximum_difference_problem(arr):
    res = arr[1] - arr[0]
    min_val = arr[0]

    for i in range(1,len(arr)):
        res = max(res, arr[i]-min_val)
        min_val = min(min_val, arr[i])

    return res


if __name__ == "__main__":
    arr = [1,10,3,4,5]
    n = maximum_difference_problem(arr)
    print(n)