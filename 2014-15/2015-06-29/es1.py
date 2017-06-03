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
from numpy.random import permutation


def min_ab(A, B):
    n = len(A)
    i = j = 1
    while i != n and j != n:
        if A[i] >= B[j]:
            i += 1
        else:
            j += 1
    return B[j]


def get_AB(max_i, s):
    a = randint(max_i, size=s)
    b = permutation(a)
    return list(a), list(b)


if __name__ == '__main__':
    m = 999999  # max int
    for s in [10, 100, 1000, 10000, 100000]:
        a, b = get_AB(m, s)
        print(min_ab(a, b))
