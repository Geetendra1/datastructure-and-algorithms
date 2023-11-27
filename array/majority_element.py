
def main(arr):
    count = 1
    res = 0

    for i in range(1,len(arr)):
        if(arr[i-1] == arr[i]):
            count += 1
        else:
            count += -1
        if (count ==0):
            count = 1
            res = i
    return res


if __name__ == "__main__":
    arr = [9,3,4,8,8]
    n = main(arr)
    print(n)

    count = 0
    for i in range(len(arr)):
        if(arr[n] == arr[i]):
            count += 1
        
    if(count > n/2):
        print('True')
    else :
        print('False')
