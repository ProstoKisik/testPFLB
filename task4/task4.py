import sys


def main(arr):
    f = open(arr, 'r')
    array = [int(x) for x in f.read().split("\n")]
    f.close()
    average = sorted(array)[len(array) // 2]
    median = sum(abs(v - average) for v in array)
    print(median)


if __name__ == '__main__':
    arg1 = sys.argv[1]
    main(arg1)
