def is_prime(n):
    if(n==1):
        return False
    i = 2
    while(i*i<=n):
        if(n%i==0):
            return False
        i = i+1
        
    return True

def main():
    number = 65
    print(is_prime(number))

if __name__ == "__main__":
    main()