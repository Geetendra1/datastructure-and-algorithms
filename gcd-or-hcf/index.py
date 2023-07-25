

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b, a%b)


a=10
b=5
def main():
    print(gcd(a,b))


if __name__ == "__main__":
    main()