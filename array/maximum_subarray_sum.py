
def main(arr):
    res = arr[0]
    max_ending = arr[0]
    for i in range(1,len(arr)):
        max_ending = max((max_ending + arr[i]),  arr[i])
        res = max(res, max_ending)
    return res


if __name__ == "__main__":
    arr = [-3,8,-2,4 -5,6]
    n = main(arr)
    print(n)