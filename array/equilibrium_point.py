
def main(arr):
    rs = 0
    for i in range(len(arr)):
            rs += arr[i]
    ls = 0
    for i in range(len(arr)):
         rs = rs-arr[i]

         if ls == rs :
              return True
         ls += arr[i]

    return False




if __name__ == "__main__":
    arr = [3,4,8,-9,9,7]
    n = main(arr)
    print(n)