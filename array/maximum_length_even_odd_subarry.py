
def max_subaaray(arr):

    res= 1
    curr = 1

    for i in range(1,len(arr)):
        if((arr[i]%2 == 0 and arr[i-1]%2 !=0) or (arr[i]%2 != 0 and arr[i-1]%2 ==0)):
            curr += 1
            res = max(res,curr)
        else:
            curr = 1
    return res
   


if __name__ == "__main__":
    arr = [5, 10,20,6,3,8]
    print(max_subaaray(arr))