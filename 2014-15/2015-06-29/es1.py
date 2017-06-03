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
    for s in [10, 100, 1000, 10000, 100000]:
    a, b = get_AB(m, s)
    print(min_ab(a, b))
