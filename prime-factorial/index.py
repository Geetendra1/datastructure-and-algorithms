def primeFactorial(n):
    if(n<=1):
        return
    i = 2
    while(i*i <=n):
        while(n%i==0):
            print(i, end=" ")
            n = n//i
        i = i+1
    if n > 1:
        print(n, end=" ")



def main():
    number = 25
    print(primeFactorial(number))


if __name__ == "__main__":
    main()