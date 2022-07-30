# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 7/30/2022
# Description: Plots the sort times for bubble and insertion sorts for ten randomly generated lists of
#               different lengths.


import time
import random
import functools

from matplotlib import pyplot


def sort_timer(func):
    """Returns the time in seconds it takes a function to run."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        return end_time - start_time
    return wrapper


def compare_sorts(wrapped_bubble, wrapped_insertion):
    """Plots the times for bubble and insertion sorts for various randomly generated lists."""

    bubble_time_list = []
    insertion_time_list = []

    for i in range(1, 11):

        r = 0
        random_list = []

        while r <= i*1000:
            random_int = random.randint(1, 10000)
            random_list.append(random_int)
            r += 1

        random_list_2 = list(random_list)

        bubble_time = wrapped_bubble(random_list)
        insertion_time = wrapped_insertion(random_list_2)

        bubble_time_list.append(bubble_time)
        insertion_time_list.append(insertion_time)

    pyplot.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], bubble_time_list, 'ro--', linewidth=2,
                label='Bubble Sort')
    pyplot.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], insertion_time_list, 'go--', linewidth=2,
                label='Insertion Sort')
    pyplot.xlabel("Length of list (in thousands)")
    pyplot.ylabel("Time taken to sort (in seconds)")
    pyplot.legend(loc='upper left')
    pyplot.show()


def bubble_sort(a_list):
    """
    Sorts a_list in ascending order
    """
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp


def insertion_sort(a_list):
    """
    Sorts a_list in ascending order
    """
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
    while pos >= 0 and a_list[pos] > value:
        a_list[pos + 1] = a_list[pos]
        pos -= 1
    a_list[pos + 1] = value


compare_sorts(sort_timer(bubble_sort), sort_timer(insertion_sort))