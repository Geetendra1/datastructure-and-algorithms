def get_largest(arr):
    n = 0
    for i in range(len(arr)):
        if arr[i] > n:
            n = arr[i]
    return n


if __name__ == "__main__":
    arr = [5, 8, 20, 21]
    print(get_largest(arr))