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
Finds shortest common super-sequence among 2 strings with dp approach.
TODO
"""

import random
import string
import time


def scs(x, y):
    """
    :param x: str
        First string
    :param y: str
        Second string
    :return: str
        Shortest common super-sequence of the 2 strings.
        Complexity O(exp(n)), with memoization: O(n²)
    """

    if len(x) == 0:
        return y

    if len(y) == 0:
        return x

    if x[-1] == y[-1]:  # last symbols are the same
        return scs(x[:-1], y[:-1]) + x[-1]  # consider only the first part and adds the last symbol

    removing_last_x = scs(x[:-1], y) + x[-1]  # scs found by removing last char of x
    removing_last_y = scs(x, y[:-1]) + y[-1]  # scs found by removing last char of y
    if len(removing_last_x) < len(removing_last_y):  # choose str with smallest length
        return removing_last_x
    else:
        return removing_last_y


def is_subseq(x, y):
    """
    :param x: str
        First string
    :param y: str
        Second string
    :return: bool
        True iff y contains x
    """

    it = iter(y)
    return all(any(c == ch for c in it) for ch in x)


def get_random_string(s, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(s))


if __name__ == '__main__':
    for s in [10, 100, 1000, 10000, 100000]:
        x = get_random_string(s, chars=string.ascii_lowercase)
        y = get_random_string(s, chars=string.ascii_lowercase)

        timer = time.time()
        scs_xy = scs(x, y)
        timer = time.time() - timer

        if is_subseq(x, scs_xy) and is_subseq(y, scs_xy):
            print("Found shortest common super-sequence of length", len(scs_xy), "in", str(timer), "seconds")
