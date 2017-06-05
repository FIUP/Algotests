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
Find n-th item in sorted array with multiple approaches.
"""

import time

from numpy.random import randint


def left_child_index(i):
    """
    :param i: int
        Index of node in array (that is organised as heap)
    :return: int
        Position in array of left child of node
    """

    return 2 * (i + 1) - 1


def get_left_child(a, i):
    """
    :param a: list
        List organized as heap
    :param i: int
        Index of node in array (that is organised as heap)
    :return: object
        Value of left child of node
    """

    child_i = left_child_index(i)
    if child_i in range(len(a)):
        return a[child_i]
    else:
        return None


def right_child_index(i):
    """
    :param i: int
        Index of node in array (that is organised as heap)
    :return: int
        Position in array of right child of node
    """

    return left_child_index(i) + 1


def get_right_child(a, i):
    """
    :param a: list
        List organized as heap
    :param i: int
        Index of node in array (that is organised as heap)
    :return: object
        Value of left child of node
    """

    child_i = right_child_index(i)
    if child_i in range(len(a)):
        return a[child_i]
    else:
        return None


def parent_index(i):
    """
    :param i: int
        Index of node in array (that is organised as heap)
    :return: int
        Position in array of parent of node
    """

    return int((i - 1) / 2)


def build_minheap(a):
    """
    :param a: list
        List of sortable objects
    :return: list
        List as minheap
    """

    b = a  # copy

    swaps = 0
    for i in range(len(b)):
        if b[i] < b[parent_index(i)]:
            b[parent_index(i)], b[i] = b[i], b[parent_index(i)]  # swap parent <-> children
            swaps += 1
    if swaps != 0:
        b = build_minheap(b)

    return b


def minheapify(a, i):
    """
    :param a: list
        List organized as minheap
    :param i: int
        Index of array
    :return: list
        List organized as true minheap. Converts to minheap if necessary.
    """

    l, l_val = left_child_index(i), get_left_child(a, i)  # position and value fo children
    r, r_val = right_child_index(i), get_right_child(a, i)

    smallest_i = i  # find index of smallest value among a[i] and its children
    if l_val is not None and l_val < a[smallest_i]:
        smallest_i = l
    if r_val is not None and r_val < a[smallest_i]:
        smallest_i = r

    if smallest_i != i:
        a[smallest_i], a[i] = a[i], a[smallest_i]  # swap
        return minheapify(a, smallest_i)

    return a


def is_min_heap(a):
    """
    :param a: list
        Array organized as max-heap
    :return: bool
        Checks if array a is a min-heap.
        Complexity: O(n)
    """

    def check_child(child, parent):
        """
        :param child: number
            Value of children of parent in a max-heap
        :param parent: number
            Value of parent in a max-heap
        :return: bool
            Check sif child is children of parent in a max-heap
        """

        if child is not None:
            return child >= parent
        else:
            return True

    for i in range(len(a)):
        parent = a[i]

        if left_child_index(i) in range(len(a)):
            l_child = a[left_child_index(i)]  # left child of node
        else:
            l_child = None

        if right_child_index(i) in range(len(a)):
            r_child = a[right_child_index(i)]  # right child of node
        else:
            r_child = None

        if (not check_child(l_child, parent)) or (not check_child(r_child, parent)):
            return False

    return True


def build_maxheap(a):
    """
    :param a: list
        List of sortable objects
    :return: list
        List as minheap
    """

    b = a  # copy

    swaps = 0
    for i in range(len(b)):
        if b[i] > b[parent_index(i)]:
            b[parent_index(i)], b[i] = b[i], b[parent_index(i)]  # swap parent <-> children
            swaps += 1
    if swaps != 0:
        b = build_maxheap(b)

    return b


def is_max_heap(a):
    """
    :param a: list
        Array organized as max-heap
    :return: bool
        Checks if array a is a max-heap.
        Complexity: O(n)
    """

    def check_child(child, parent):
        """
        :param child: number
            Value of children of parent in a max-heap
        :param parent: number
            Value of parent in a max-heap
        :return: bool
            Check sif child is children of parent in a max-heap
        """

        if child is not None:
            return child <= parent
        else:
            return True

    for i in range(len(a)):
        parent = a[i]

        if left_child_index(i) in range(len(a)):
            l_child = a[left_child_index(i)]  # left child of node
        else:
            l_child = None

        if right_child_index(i) in range(len(a)):
            r_child = a[right_child_index(i)]  # right child of node
        else:
            r_child = None

        if (not check_child(l_child, parent)) or (not check_child(r_child, parent)):
            return False

    return True


def maxheapify(a, i):
    """
    :param a: list
        List organized as maxheap
    :param i: int
        Index of array
    :return: list
        List organized as true maxheap. Converts to maxheap if necessary.
    """

    l, l_val = left_child_index(i), get_left_child(a, i)  # position and value fo children
    r, r_val = right_child_index(i), get_right_child(a, i)

    largest_i = i  # find index of smallest value among a[i] and its children
    if l_val is not None and l_val > a[i]:
        largest_i = l
    if r_val is not None and r_val > a[largest_i]:
        largest_i = r

    if largest_i != i:
        a[largest_i], a[i] = a[i], a[largest_i]  # swap
        return maxheapify(a, largest_i)

    return a


def select_naive(a, k):
    """
    :param a: list
        List of sortable objects
    :param k: int
        Index in array
    :return: []
        Object in n-th position in sorted array.
        Quick-sort and take n-th element. Complexity O(nlogn)
    """

    return sorted(a)[k]


def select_minheap(a, k):
    """
    :param a: list
        List of sortable objects
    :param k: int
        Index in array
    :return: []
        Object in n-th position in sorted array.
        Build min-heap. Remove the root (which is the smallest element) k - 1 times: the new root is the k-th smallest.
        Complexity O(n + klogn)
    """

    b = build_minheap(a)
    for _ in range(k):  # remove k - 1 times the root
        b[0] = float("inf")  # remove root
        b = minheapify(b, 0)  # restore minheap condition
    return b[0]


def select_maxheap(a, k):
    """
    :param a: list
        List of sortable objects
    :param k: int
        Index in array
    :return: []
        Object in n-th position in sorted array.
        Build fixed size max-heap of size k, iterate through each item in array and push to heap, then pop. Complexity O(nlogk)
    """

    b = build_maxheap(a[:k + 1])  # max heap of first k elements
    for i in range(k + 1, len(a)):
        if a[i] < b[0]:
            b[0] = a[i]  # replace root
            b = maxheapify(b, 0)  # restore maxheap condition

    return b[0]


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
    for s in [10, 100, 1000, 10000]:
        a = get_random_list(s)
        k = randint(0, s)  # random index
        k_smallest_val = sorted(a)[k]

        timer = time.time()
        k_val = select_maxheap(a, k)
        timer = time.time() - timer

        if k_smallest_val == k_val:
            print("Found", str(k) + "-th smallest element in sorted array:", k_val)
            print("Time taken:", timer, "seconds")
