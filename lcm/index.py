
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b, a%b)

def lcm(a,b):
    return (a*b)//gcd(a,b)


def main():
    a = 6
    b = 4
    print(lcm(a, b))


if __name__ == "__main__":
    main()