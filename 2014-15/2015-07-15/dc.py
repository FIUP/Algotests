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


from random import random


class RedBlackTreeNode(object):
    """ Node of a Red-Black tree """

    RED = "red"  # possible colors of node
    BLACK = "black"

    def __init__(self, key, color, left=None, right=None):
        """
        :param key: number
            Value of node
        :param color: str
            Color of node (either red or black)
        :param left: RedBlackTreeNode
            Node at the left of this node
        :param right: RedBlackTreeNode
            Node at the right of this node
        """

        object.__init__(self)

        self.key = float(key)

        if not (color == RedBlackTreeNode.RED or color == RedBlackTreeNode.BLACK):
            raise ValueError(color + " must be either " + RedBlackTreeNode.RED + " either " + RedBlackTreeNode.BLACK)

        self.color = str(color)
        self.left = left
        self.right = right

    def is_red(self):
        """
        :return: bool
            Checks whether node is red
        """

        return self.color == RedBlackTreeNode.RED

    def is_black(self):
        """
        :return: bool
            Checks whether node is black
        """

        return self.color == RedBlackTreeNode.BLACK


def count_black_height(t):
    """
    :param t: RedBlackTreeNode
        Root of a Red-Black tree
    :return: int
        Number of black nodes in each path to each leaf.
        Each path contain the same quantity of black nodes, so take a random direction each time (left or right) until
        you reach leaf and count black nodes.
        Complexity: O(log(n)), n is the number of nodes in tree.
    """

    if t is None:  # out of bounds (should not happen)
        return 0

    count_black = 1 if t.is_black() else 0  # check if this node is black

    if t.right is None:  # must go left
        return count_black + count_black_height(t.left)

    if t.left is None:  # must go right
        return count_black + count_black_height(t.right)

    # can choose whatever direction I want
    if random() < 0.5:  # go left
        return count_black + count_black_height(t.left)
    else:  # go right
        return count_black + count_black_height(t.right)


def black_height(t):
    """
    :param t: RedBlackTreeNode
        Root of a Red-Black tree
    :return: int
        Checks all paths from root to all leaves contain the same quantity black nodes.
        Returns -1 if not all leaves contain the same quantity black node, else the number of black nodes.
        Complexity: O(2^log(n)) = O(n), n is the number of nodes in tree
    """

    if t is None:
        return 0

    going_right_blacks = black_height(t.right)  # go right and count blacks
    going_left_blacks = black_height(t.left)  # go left and count blacks

    if (going_right_blacks == -1 or going_left_blacks == -1) or (going_left_blacks != going_right_blacks):
        return -1  # subtrees are wrong
    else:
        count_black = 1 if t.is_black() else 0  # check if this node is black
        return count_black + going_left_blacks


if __name__ == '__main__':
    n0 = RedBlackTreeNode(6, RedBlackTreeNode.RED)  # leaf
    n1 = RedBlackTreeNode(0, RedBlackTreeNode.RED)  # first-level left
    n2 = RedBlackTreeNode(219, RedBlackTreeNode.RED, left=n0)  # first-level right
    n3 = RedBlackTreeNode(5, RedBlackTreeNode.BLACK, left=n1, right=n2)  # root
    # the tree now looks like
    #      n3 (b)
    #     /     \
    #  n1 (r)   n2 (r)
    #          /
    #        n0 (r)
    print(black_height(n3))  # 1

    n2 = RedBlackTreeNode(219, RedBlackTreeNode.BLACK, left=n0)  # first-level left
    n3 = RedBlackTreeNode(5, RedBlackTreeNode.RED, left=n1, right=n2)  # root
    # the tree now looks like
    #      n3 (r)
    #     /     \
    #  n1 (r)   n2 (b)
    #          /
    #        n0 (r)
    print(black_height(n3))  # -1
