from matplotlib import pyplot as plt


def bubble_sort(lst):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lst) - 1):

            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

                swapped = True

    return lst


def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j

        arr[minimum], arr[i] = arr[i], arr[minimum]
    return arr


def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > cursor:
            # Меняем местами число, продвигая по списку
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Остановимся и сделаем последний обмен
        arr[pos] = cursor

    return arr