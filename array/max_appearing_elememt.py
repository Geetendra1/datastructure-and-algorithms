MAX = 100
def main(L,R,n):
     freq = [0] * MAX

     for i in range(n):
         freq[L[i]]+= 1
         freq[R[i]+1]-= 1
     
     
     res = 0

     for i in range(n):
        freq[i] = freq[i-1] + freq[i]
        if(freq[i] > res):
            res = i

     return res



if __name__ == "__main__":
    L = [1, 4, 9, 13, 21]
    R = [15, 8, 12, 20, 30]
    n = len(L)

    print(main(L, R, n))