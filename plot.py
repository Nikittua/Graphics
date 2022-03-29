import random
import time
import timeit
from typing import List

from matplotlib import pyplot

from algos import bubble_sort

import matplotlib.pyplot as plt

Y = []
X = []


# 10 20 30 40 50 60 .... 200: sizes
# y1 y2 y3 y4 y5 y6..... yn: time


def random_gen(n: int) -> list[int]:
    return [random.randint(1, 1000) for _ in range(n)]


def benchmark(func: 'Function', arr: list) -> 'time':
    start = time.time_ns()
    sorted_arr = func(arr)
    return time.time_ns() - start


def main():
    global X, Y
    sort_func = bubble_sort

    for size in range(1000):
        X.append(size)
        arr = random_gen(size)
        Y.append(benchmark(sort_func, arr))
    values = Y

    plt.plot(X, Y, color='red')
    plt.xlabel('Number of elements ')
    plt.ylabel('time')
    # pyplot.xlim([0, 500])
    # pyplot.ylim([0, 1])
    plt.show()


if __name__ == "__main__":
    main()
