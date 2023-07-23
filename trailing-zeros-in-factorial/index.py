def tz(n):
    res = 0

    i = 5

    while i <= n:
    # The line `res = res + n // i` is adding the integer division of `n` by `i` to the current value
    # of `res`. The `//` operator performs integer division, which means it returns the quotient of the
    # division without the decimal part.
        res = res + n // i
        i = i*5
    return res
def main():
    number = 100
    print(tz(number))

if __name__ == "__main__":
    main()
