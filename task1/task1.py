

def main(n, m: int):
    s = 1
    while True:
        print(s, end='')
        s = 1 + (s + m - 2) % n
        if s == 1:
            break


if __name__ == '__main__':
    a, b = map(int, input().split())
    main(a, b)
