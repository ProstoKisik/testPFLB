import math
import sys


def main(file1, file2):
    f = open(file1, 'r')
    center, radius = f.read().split("\n")
    centerX, centerY = center.split(" ")
    radius = int(radius)
    f.close()

    f = open(file2, 'r')
    while True:
        line = f.readline()
        if not line:
            break
        pointX, pointY = line.split(" ")

        d = math.sqrt(math.pow((float(pointX) - float(centerX)), 2) + math.pow((float(pointY) - float(centerY)), 2))
        d = math.fabs(d)
        print(d)

        if d == radius:
            print('0')

        if d < radius:
            print('1')

        if d > radius:
            print('2')
    f.close()


if __name__ == '__main__':
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]

    main(arg1, arg2)
