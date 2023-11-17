def maximum_consicutive_ones(arr):
    res = 0
    curr = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            curr = 0
        else :
            curr += 1
            res = max(res,curr)
    return res




if __name__ == "__main__":
    arr = [1,1,1,0,0,0,1]
    print(maximum_consicutive_ones(arr))