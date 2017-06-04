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


from numpy.random import permutation
from numpy.random import randint


def min_ab(A, B):
    """
    :param A: list
        List of numbers
    :param B: list
        Random permutation of A
    :return: number
        Minimum of A (and also B) found by not-comparing elements of the same array.
        Complexity: O(n)
    """

    n = len(A)
    i = j = 1
    while i != n and j != n:
        if A[i] >= B[j]:
            i += 1
        else:
            j += 1
    return B[j]


def get_AB(s, m=999999):
    """
    :param s: int
        Size of output arrays
    :param max_i: int
        Max number in arrays
    :return: list, list
        A random list, a random permutation of first list
    """

    a = randint(max_i, size=s)
    b = permutation(a)
    return list(a), list(b)


if __name__ == '__main__':
    for s in [10, 100, 1000, 10000, 100000]:
        a, b = get_AB(s)
        print(min_ab(a, b))
