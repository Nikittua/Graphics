import random
import time
import algos
import matplotlib.pyplot as plt


class Graphic:
    Y = []
    X = []

    def random_gen(n: int) -> list[int]:
        return [random.randint(1, 1000) for _ in range(n)]

    @staticmethod
    def benchmark(func: 'Function', arr: list) -> 'time':
        start = time.time_ns()
        sorted_arr = func(arr)
        return time.time_ns() - start

    @staticmethod
    def display(sort_func: 'Function', iterations: int):
        for size in range(iterations):
            Graphic.X.append(size)  # Количество элементов
            arr = Graphic.random_gen(size)  # список отсортированных рандомных значений
            k = Graphic.benchmark(sort_func, arr)
            Graphic.Y.append(k)  # время сортировки этих значений
        plt.xlabel('Number of elements ')
        plt.ylabel('Time')
        plt.plot(Graphic.X, Graphic.Y, color='red')
        plt.show()


a = Graphic()
a.display(algos.bubble_sort, 1000)
