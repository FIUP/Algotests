# !/usr/bin/python3
# coding: utf-8

# Copyright 2017 Stefano Fogarollo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""
Find number of pairs (i, j) such that i < j and a[i] > a[j] with a divide-et-impera approach.
Hint: edit mergesort.
"""

import sys
import time

from numpy.random import randint


def inv_sort(a):
    """
    :param a: list
        List of sortable objects (e.g numbers)
    :return: list, int
        Sorted list and number of such i, j pairs
        Complexity O(nlogn)
    """

    if len(a) <= 1:  # a already sorted
        return a, 0

    split_index = int(len(a) / 2)
    left_part, left_swaps = inv_sort(a[0: split_index])  # sort
    right_part, right_swaps = inv_sort(a[split_index: len(a)])
    merged_list, swaps_number = inv_merge(left_part, right_part)  # merge
    return merged_list, swaps_number + left_swaps + right_swaps


def inv_merge(a, b):
    """
    :param a: list
        List of sorted objects (e.g numbers)
    :param b: list
        List of sorted objects (e.g numbers)
    :return: list, list
        Sorted list a + b and number of such i, j pairs
        Complexity O(n)
    """

    swaps_number = 0  # number of swaps
    for a_val in a:
        for b_val in b:
            if a_val > b_val:
                swaps_number += 1

    merged_list = []  # list containing sorted a + b
    index_a = index_b = 0  # indexes to go through lists
    while index_a < len(a) or index_b < len(b):
        if index_a not in range(len(a)):  # a does not contain anything
            merged_list.append(b[index_b])
            index_b += 1
        elif index_b not in range(len(b)):  # b does not contain anything
            merged_list.append(a[index_a])
            index_a += 1
        else:
            if a[index_a] < b[index_b]:
                merged_list.append(a[index_a])
                index_a += 1
            elif a[index_a] == b[index_b]:
                merged_list.append(a[index_a])
                merged_list.append(b[index_b])
                index_a += 1
                index_b += 1
            else:
                merged_list.append(b[index_b])
                index_b += 1

    return merged_list, swaps_number


def inv_naive(a):
    """
    :param a: list
        List of sorted objects (e.g numbers)
    :return: int
        Number of such i, j pairs
        Complexity O(n²)
    """

    swaps_counter = 0
    for j in range(len(a)):
        for i in range(j):
            if a[i] > a[j]:
                swaps_counter += 1
    return swaps_counter


def get_random_list(length, m=999999):
    """
    :param length: int
        Size of output arrays
    :param m: int
        Max number in arrays
    :return: list
            A random list such that last - first > len(list)
    """

    return list(randint(m, size=length))


if __name__ == '__main__':
    sys.setrecursionlimit(100000)  # let recursion happen

    for s in [10, 100, 1000, 10000]:
        a = get_random_list(s)

        timer = time.time()
        a, swaps_count = inv_sort(a)
        timer = time.time() - timer

        print("Counted", swaps_count, "swaps in", str(timer), "seconds")
