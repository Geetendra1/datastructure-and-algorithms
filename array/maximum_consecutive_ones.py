
def main(arr):
    res = 0 
    count = 0
    for i in range(len(arr)):
        if(arr[i]!= 0):
            count += 1
            res = max(res,count)
        else :
            count = 0
    print('res',res)

if __name__ == "__main__":
    arr = [1,1,0,0,0,1,1,1]
    n = main(arr)
    print(n)