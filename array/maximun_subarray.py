def max_subaaray(arr):
    res = arr[0]
    max_ending = arr[0]


    for i in range(1, len(arr)):
        max_ending = max(max_ending + arr[i], arr[i])
        print('max_ending',max_ending)
        res = max(res, max_ending)
        print('res',res)
        print('----------------------')
    return res

if __name__ == "__main__":
    arr = [5, 8, -22, 2]
    print(max_subaaray(arr))

# res = 0, max_ending = 0
# i = 1, max_ending = max(5+8, 8) => 13, res = max(5,13) => 13
# i = 2, max_ending = max(13-22, -22) => -9, res = max(-9,13) => 13
# i = 3, max_ending = max(-9+2, 2) => 2, res = max(2,13) => 13