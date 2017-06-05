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


""" Recursive version of classic Insertion Sort algorithm """

import sys
import time

from numpy.random import randint


def recursive_insertion_sort(a, end=0):
    """
    :param a: list
        List of sortable objects (e.g numbers)
    :param end: int
        Index to end sorting
    :return: list
        Sorted list up to a[end]
        Complexity O(n²)
    """

    if end not in range(len(a)):  # out of bounds -> algorithm done!
        return a

    # a[0 : end - 1] is sorted, now sort also a[end]
    index_of_item_to_sort = end  # index of element to sort
    for i in range(end - 1, -1, -1):  # cycle through all sorted elements of a
        if a[i] > a[index_of_item_to_sort]:
            tmp = a[i]
            a[i] = a[index_of_item_to_sort]
            a[index_of_item_to_sort] = tmp  # swap
            index_of_item_to_sort = i  # update new index
        else:  # item to sort is in sorted place -> stop
            break

    return recursive_insertion_sort(a, end=end + 1)  # sort new item


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
    sys.setrecursionlimit(1000000)  # let recursion happen

    for s in [10, 100, 1000, 10000, 100000]:
        a = get_random_list(s)

        timer = time.time()
        a = recursive_insertion_sort(a)
        timer = time.time() - timer

        if a == sorted(a):
            print("Sorted", len(a), "items in", str(timer), "s")
