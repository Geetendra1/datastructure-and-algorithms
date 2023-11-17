def remove_duplicate_i_sorted_array(arr):
    res = 1
    for i in range(len(arr)):
        if arr[i] != arr[res - 1]:
            arr[res] = arr[i]
            res += 1
    return res


if __name__ == "__main__":
    arr = [10,10,10, 20, 21,21,21]
    n = remove_duplicate_i_sorted_array(arr)

    for i in range(n):
        print(arr[i])