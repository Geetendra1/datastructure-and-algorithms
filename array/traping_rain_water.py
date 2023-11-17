def traping_rain_water(arr):
    n = len(arr)
    res= 0 
    lmax = [0]*n
    lmax[0] = arr[0]
    for i in range(1,n):
        lmax[i] = max(arr[i], lmax[i-1])
    
    rmax = [0]*n
    rmax[n-1] = arr[n-1]
    for i in range(n-2, -1,-1):
        rmax[i]  = max(arr[i], rmax[i+1])
    
    for i in range(1,n-1):
        res = res+(min(rmax[i], lmax[i])-arr[i])
    return res
    # print(lmax[0])
if __name__ == "__main__":
    arr = [5, 0, 6, 2, 3]
    print(traping_rain_water(arr))