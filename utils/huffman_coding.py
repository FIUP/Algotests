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
Pythonic way to calculate prefix codes based on Huffman algorithm.
"""

import queue


class HuffmanNode(object):
    """ Node of Huffman tree """

    def __init__(self, left=None, right=None):
        """
        :param left: HuffmanNode
            Left children of node
        :param right: HuffmanNode
            Right children of node
        """

        object.__init__(self)

        self.left = left
        self.right = right

    def children(self):
        """
        :return: tuple (HuffmanNode, HuffmanNode)
            Children of node
        """

        return self.left, self.right


def create_huffman_tree(frequencies):
    """
    :param frequencies: list of tuple float, str
        List of pair (frequency of letter, letter)
    :return: HuffmanNode
        Huffman tree of frequencies
    """

    p = queue.PriorityQueue()
    for v in frequencies:  # create a leaf node for each symbol and add it to the priority queue
        p.put(v)

    while p.qsize() > 1:  # while there is more than one node
        l, r = p.get(), p.get()  # remove two highest nodes
        n = HuffmanNode(left=l, right=r)  # create internal node with children
        p.put((l[0] + r[0], n))  # add new node to queue

    return p.get()  # return root node


def walk_tree(n, prefix="", c={}):
    """
    :param n: HuffmanNode
        Tree to traverse
    :param prefix: str
        Prefix of each symbol
    :param c: dic string -> string
        Huffman encoding of alphabet
    :return: dict string -> string
        Recursively walk the tree down to the leaves, assigning a code value to each symbol
    """

    if isinstance(n[1].left[1], HuffmanNode):
        walk_tree(n[1].left, prefix + "0", c)
    else:
        c[n[1].left[1]] = prefix + "0"

    if isinstance(n[1].right[1], HuffmanNode):
        walk_tree(n[1].right, prefix + "1", c)
    else:
        c[n[1].right[1]] = prefix + "1"

    return c


def calc_avg_word(frequencies, c):
    """
    :param frequencies: list of tuple float, str
        List of pair (frequency of letter, letter)
    :param c: dict
        Huffman encoding
    :return: float
        Average string length
    """

    freq_dict = {k: v for v, k in frequencies}  # get dict structure
    tot_avg = 0
    tot_freq = sum(freq_dict.values())
    for k in freq_dict:
        word_avg = len(c[k]) * freq_dict[k] / tot_freq
        tot_avg += word_avg
    return tot_avg


if __name__ == '__main__':
    freq = [
        (8.167, "a"), (1.492, "b"), (2.782, "c"), (4.253, "d"), (12.702, "e"), (2.228, "f"), (2.015, "g"), (6.094, "h"),
        (6.966, "i"), (0.153, "j"), (0.747, "k"), (4.025, "l"), (2.406, "m"), (6.749, "n"), (7.507, "o"), (1.929, "p"),
        (0.095, "q"), (5.987, "r"), (6.327, "s"), (9.056, "t"), (2.758, "u"), (1.037, "v"), (2.365, "w"), (0.150, "x"),
        (1.974, "y"), (0.074, "z")
    ]

    node = create_huffman_tree(freq)  # create huffman tree
    code = walk_tree(node)

    for i in sorted(freq, reverse=True):
        print(i[1], "{:6.2f}".format(i[0]), code[i[1]])

    print("Average word length is", calc_avg_word(freq, code))
