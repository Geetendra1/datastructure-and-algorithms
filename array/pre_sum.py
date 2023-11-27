
def get_sum(ps, l, r):
    if l == 0:
        return ps[r]
    return ps[r] - ps[l - 1]

def main():
    arr = [2, 8, 3, 9, 6, 5, 4]
    n = 7
    ps = [0] * n
    ps[0] = arr[0]
    for i in range(1, n):
        ps[i] = ps[i - 1] + arr[i]
    print(get_sum(ps, 1, 3))

if __name__ == "__main__":
    main()