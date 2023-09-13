import argparse
import math


def make_pascal_triangle(n: int):
    triangle = [[], []]
    triangle[0].append(1)
    triangle[1].append(1)
    triangle[1].append(1)
    for i in range(2, n):
        triangle.append([])
        for j in range(len(triangle[i - 1]) + 1):
            if j == 0:
                fst_parent = 0
            else:
                fst_parent = triangle[i - 1][j - 1]
            if j == len(triangle[i - 1]):
                snd_parent = 0
            else:
                snd_parent = triangle[i-1][j]

            triangle[i].append(fst_parent + snd_parent)
    for i in range(len(triangle)):
        triangle[i] = " ".join(map(str, triangle[i]))
        triangle[i] = " " * (n - i) + triangle[i]
    return triangle


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='type height of pascal triangle')
    parser.add_argument('n', metavar='N', type=int)
    args = parser.parse_args()
    n_arg = args.n
    triangle = make_pascal_triangle(n_arg)
    for line in triangle:
        print(line)
