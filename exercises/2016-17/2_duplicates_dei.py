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


""" Find duplicates in array with Divide-Et-Impera approach.
Solution: like mergesort ... but when merging, check if max left != min right.
"""

import sys
import time

from numpy.random import randint


def dup_sort(a):
    """
    :param a: list
        List of sortable objects (e.g numbers)
    :return: list, list of duplicates
        Sorted list and list of duplicates found
        Complexity O(nlogn)
    """

    if len(a) <= 1:  # a already sorted
        return a, []

    split_index = int(len(a) / 2)
    left_part, left_dups = dup_sort(a[0: split_index])  # sort
    right_part, right_dups = dup_sort(a[split_index: len(a)])
    return dup_merge(left_part, right_part)  # merge


def dup_merge(a, b):
    """
    :param a: list
        List of sorted objects (e.g numbers)
    :param b: list
        List of sorted objects (e.g numbers)
    :return: list, list of duplicates
        Sorted list a + b and list of duplicates found
        Complexity O(n)
    """

    merged_list = []  # list containing sorted a + b
    dups_list = []  # list containing duplicates
    index_a = index_b = 0  # indexes to go through lists

    while index_a < len(a) or index_b < len(b):
        if index_a not in range(len(a)):  # a does not contain anything
            merged_list.append(b[index_b])
            index_b += 1
        elif index_b not in range(len(b)):  # a does not contain anything
            merged_list.append(a[index_a])
            index_a += 1
        else:
            if a[index_a] < b[index_b]:
                merged_list.append(a[index_a])
                index_a += 1
            elif a[index_a] == b[index_b]:
                merged_list.append(a[index_a])
                merged_list.append(b[index_b])
                dups_list.append(a[index_a])  # add duplicate to list
                index_a += 1
                index_b += 1
            else:
                merged_list.append(b[index_b])
                index_b += 1

    return merged_list, dups_list


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
        a = get_random_list(s, m=s / 2)

        timer = time.time()
        a, duplicates = dup_sort(a)
        timer = time.time() - timer

        if a == sorted(a):
            print("Sorted", len(a), "items in", str(timer), "s")
            print("Found", len(duplicates), "duplicates")
