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
Find i, j in array such that a[i] + a[j] = key
Solution: hash each item in array and find index x such that hash(key - a[x]) != x.
"""

import sys
import time

from numpy.random import randint


def sum_key(a, k):
    """
    :param a: list
        List of numbers
    :param k: number
        Number to check if a[i] + a[j] = k for some i, j
    :return: []
        List of such i, j
        Complexity O(n)
    """

    such_ijs = []
    hashed_values = {}  # dictionary a[i] -> i
    for i in range(len(a)):
        hashed_values[a[i]] = i

    for i in range(len(a)):
        if k - a[i] in hashed_values and hashed_values[k - a[i]] != i:
            such_ijs.append((i, hashed_values[k - a[i]]))

    return such_ijs


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
        k = randint(min(a), int(max(a) + min(a) * 2))

        timer = time.time()
        such_ijs = sum_key(a, k)
        timer = time.time() - timer

        print("Found", len(such_ijs), "pair of (i, j) such that a[i] + a[j] =", k)
        for p in such_ijs:
            print(p, (a[p[0]], a[p[1]]), a[p[0]] + a[p[1]])
