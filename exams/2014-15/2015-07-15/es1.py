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


from numpy.random import randint


def find_a_gap(a, start, end):
    """
    :param a: list
        List of numbers
    :param start: int
        Index to start searching from
    :param end: int
        Index to end searching for a gap
    :return: int
        Gap of a (i such that a[i + 1] - a[i] > 1. Divide-et-impera.
        Complexity
            T(n) = 3 * O(1) + 2 * T(n - 1)
                 = O(1) + 2T(n - 1)
                 = O(n)
    """

    if start >= end:  # out of bounds
        return None

    if a[start + 1] - a[start] > 1:  # check gap from start
        return start

    if a[end] - a[end - 1] > 1:  # check gap from end
        return end - 1

    # no gap found -> check inner array
    gap_from_start = find_a_gap(a, start + 1, end)
    gap_from_end = find_a_gap(a, start, end - 1)

    if gap_from_start is None:  # no gap from start
        return gap_from_end
    else:  # possible gap from end
        return gap_from_start


def get_a(length, m=999999):
    """
    :param length: int
        Size of output arrays
    :param m: int
        Max number in arrays
    :return: list
            A random list such that last - first > len(list)
    """

    random_list = list(randint(m, size=length))
    if random_list[-1] - random_list[0] < length:
        random_list[-1] = random_list[0] + length + 1  # edit last element if necessary

    return random_list


if __name__ == '__main__':
    for s in [10, 100, 1000, 10000, 100000]:
        a = get_a(s)
        print(find_a_gap(a, 0, len(a) - 1))
