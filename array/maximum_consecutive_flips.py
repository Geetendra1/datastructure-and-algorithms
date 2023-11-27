def main(arr):
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            if arr[i] != arr[0]:
                print('from', i)
            else:
                print('t0', i-1)

    if(arr[len(arr) -1] != arr[0]):
        print('to', len(arr) -1)


if __name__ == "__main__":
    arr = [0,0,1,1,0,0,1]
    n = main(arr)
    print(n)