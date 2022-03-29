from matplotlib import pyplot as plt


def bubble_sort(lst):
    swapped = True
    total_iteration = 0
    iterarr = []
    quantity = list(range(1, len(lst) + 1))
    while swapped:
        swapped = False
        for i in range(len(lst) - total_iteration - 1):

            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

                swapped = True
        total_iteration += 1
        iterarr.append(total_iteration)
    return lst

