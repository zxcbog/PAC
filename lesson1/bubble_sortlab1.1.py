import argparse


def bubble_sort(arr: list):
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('arr', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    args = parser.parse_args()
    arr_to_sort = args.arr
    bubble_sort(arr_to_sort)
    print(arr_to_sort)
