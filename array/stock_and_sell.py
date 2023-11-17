
def stock_by_and_sell(arr):
    n = len(arr)
    profit = 0

    for i in range(n):
        if(arr[i] > arr[i-1]):
            profit = profit + (arr[i] - arr[i -1])
    return profit
        


if __name__ == "__main__":
    arr = [5, 8, 20, 22, 21]
    print(stock_by_and_sell(arr))