#lab 2.1 + 2.2
import argparse
import numpy as np


#кастомные исключения(прост для красоты)
class DotException(Exception):
    def __str__(self):
        return "Количество столбцов матрицы A != количеству строк матрицы B"
class ConvolveException(Exception):
    def __str__(self):
        return "Входная матрица меньше ядра свертки"
class OperationException(Exception):
    def __str__(self):
        return "Выбрана некорректная операция"


def get_matrices(input_path):
    '''получаем матрицы из файла'''
    with open(input_path, "r") as f:
        lines = f.readlines()
        matrices = [[[]], [[]]]
        num_of_matrix = 0
        cur_i = 0
        for line in lines:
            if line == "\n":
                matrices[num_of_matrix].pop()
                cur_i = 0
                num_of_matrix += 1
                continue
            vals = line.split(" ")
            for val in vals:
                matrices[num_of_matrix][cur_i].append(int(val))
                if "\n" in val:
                    cur_i += 1
                    matrices[num_of_matrix].append([])
    return matrices[0], matrices[1]


def put_matrices(output_path, matrix):
    '''записываем новую матрицу в файл'''
    with open(output_path, "w") as f:
        for line in matrix:
            for val in line:
                f.write(f"{val} ")
            f.write("\n")


def dot(a: list, b: list):
    '''перемножение двух матриц(если столбцы(A) != строки(B) - рейзим исключение)'''
    if len(a[0]) != len(b):
        raise DotException

    c = [[]]

    for i in range(len(a)):
        for j in range(len(b[i])):

            new_val = 0
            for k in range(len(a[i])):
                new_val += a[i][k] * b[k][j]

            c[i].append(new_val)
        c.append([])
    c.pop()
    return c


def convolve(matrix, core):
    '''свертка матрицы по ядру'''
    if len(matrix) < len(core) or len(matrix[0]) < len(core[0]):
        raise ConvolveException

    convolved_matrix = [[]]

    for i in range(len(matrix) - (len(core) - 1)):
        for j in range(len(matrix[i]) - (len(core[0]) - 1)):

            convolved_value = 0

            for step_i in range(len(core)):
                for step_j in range(len(core[step_i])):
                    convolved_value += core[step_i][step_j] * matrix[i + step_i][j + step_j]

            convolved_matrix[i].append(convolved_value)

        convolved_matrix.append([])
    convolved_matrix.pop()

    return convolved_matrix


def main():
    parser = argparse.ArgumentParser(description='matrices multiply(just give give in/out file paths)')
    parser.add_argument('operation', metavar='operation', type=str,
                        help='operation (dot or convolve)')
    parser.add_argument('in_path', metavar='in_path', type=str,
                        help='in path')
    parser.add_argument('out_path', metavar='out_path', type=str,
                        help='out path')

    args = parser.parse_args()
    if args.operation not in ['dot', 'convolve']:
        raise OperationException

    in_path = args.in_path
    out_path = args.out_path

    matrix1, matrix2 = get_matrices(in_path)
    out_matrix = [[]]
    if args.operation == 'dot':
        #out_matrix = np.dot(matrix1, matrix2).tolist()
        out_matrix = dot(matrix1, matrix2)
    elif args.operation == 'convolve':
        out_matrix = convolve(matrix1, matrix2)

    put_matrices(out_path, out_matrix)


if "__main__" == __name__:
    main()
