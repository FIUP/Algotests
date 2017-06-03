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


def left_child_index(i):
    """ Position in array of left child of node """

    return 2 * (i + 1) - 1


def right_child_index(i):
    """ Position in array of right child of node """

    return left_child_index(i) + 1


def check_child(child, parent):
    """ Check if child is children of parent in a max-heap """

    if child is not None:
        return child < parent
    else:
        return True


def is_max_heap(a):
    """ Check if array a is a max-heap """

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


if __name__ == '__main__':
    print(is_max_heap([10, 9, 8, 7, 6]))  # True
    print(is_max_heap([10, 9, 8, 7, 11]))  # False
