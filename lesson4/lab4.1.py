#Лабораторная работа 4.1. Выбор случайных элементов массива
#Есть два набора данных: реальные и синтетические. Допустим, мы хотим обучить некоторую ML модель на смеси реальных и синтетических данных.
#При этом синтетические данные должны браться с вероятностью P.
#Важно сохранять порядок входных чисел.
#Например: Для массивов: [1,2,3,4,5,7,8,9,10] и [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10] и P=0.2
#Один из вариантов возвращаемого значения: [1,-2,3,4,-5,6,7,8,9,10]
#
#Массивы реальных и синтетических данных одинаковой длины.
#
#Реализовать скрипт random_select.py
#Входные параметры скрипта: пути к двум файлам со списком целых чисел в каждом. Например file_1.txt содержит:
#1 2 3 4 5 6 7
#а file_2.txt
#-1 -2 -3 -4 -5 -6 -7
#
#Также в качестве аргумента командной строки передаётся вероятность P от 0 до 1.
#Результат перемешивания массивов вывести на экран.
import numpy as np
import random
import argparse


def selector(val1, val2, P):
    if random.randint(0, 100) / 100 > P:
        return val1
    else:
        return val2


def random_select(data_pack1, data_pack2, P):
    if len(data_pack1) == 0 or len(data_pack2) == 0:
        return []
    selector_vector = np.vectorize(selector)

    return selector_vector(data_pack1, data_pack2, P)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('input1', type=str, help='filepath to the first input file')
    parser.add_argument('input2', type=str, help='filepath to the second input file')
    parser.add_argument('P', type=float, help='probability of taking data from the second input file. need to be in range [0,1]')

    args = parser.parse_args()

    if '.txt' not in args.input1 or '.txt' not in args.input2 or 0 < args.P > 1:
        raise ValueError

    probability = args.P

    with open(args.input1, "r") as f:
        line = f.readline()
        real_data = np.array(list(map(lambda x: int(x), line.split(" "))))
    with open(args.input2, "r") as f:
        line = f.readline()
        synth_data = np.array(list(map(lambda x: int(x), line.split(" "))))

    print(random_select(real_data, synth_data, probability))

