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


class BinaryTreeNode(object):
    """ Node of a Red-Black tree """

    def __init__(self, key, left=None, right=None):
        """
        :param key: number
            Value of node
        :param left: RedBlackTreeNode
            Node at the left of this node
        :param right: RedBlackTreeNode
            Node at the right of this node
        """

        object.__init__(self)

        self.key = float(key)
        self.left = left
        self.right = right


def longest_path_to_leaf(t):
    """
    :param t: BinaryTreeNode
        Node of a binary tree
    :return: int
        Path to longest leaf
    """

    if t is None:  # out of bounds (should not happen)
        return 0

    if t.left is None and t.right is None:  # it's a leaf
        return 1

    if t.left is None:  # possible path is a must-go-right choice
        return 1 + longest_path_to_leaf(t.right)

    if t.right is None:  # possible path is a must-go-left choice
        return 1 + longest_path_to_leaf(t.left)

    return 1 + max(
        longest_path_to_leaf(t.right),
        longest_path_to_leaf(t.left)
    )


def is_complete(t):
    """
    :param t: BinaryTreeNode
        Node of a binary tree
    :return: bool
        True iff each node in tree has 2 children, and each leaf is at the same distance of all others
    """

    if (t.left is None and t.right is not None) or (t.left is not None and t.right is None):  # node has only 1 children
        return False

    if t.left is None and t.right is None:  # this is a leaf
        return True

    if is_complete(t.left) and is_complete(t.right):  # node has 2 children
        return longest_path_to_leaf(t.left) == longest_path_to_leaf(t.right)
    else:  # one subtree (right or left) is not complete -> thus the entire tree is not complete
        return False


if __name__ == '__main__':
    n4 = BinaryTreeNode(16)  # leaf
    n0 = BinaryTreeNode(6)  # leaf
    n1 = BinaryTreeNode(0)  # first-level left
    n2 = BinaryTreeNode(219, left=n0, right=n4)  # first-level right
    n3 = BinaryTreeNode(5, left=n1, right=n2)  # root

    # tree now looks like
    #      n3
    #     /  \
    #   n1    n2
    #        /  \
    #      n0    n4

    print(is_complete(n3))  # False
    print(is_complete(n1))  # True
    print(is_complete(n2))  # True

    n5 = BinaryTreeNode(9)
    n6 = BinaryTreeNode(7)
    n1 = BinaryTreeNode(0, left=n5, right=n6)  # first-level left
    n3 = BinaryTreeNode(5, left=n1, right=n2)  # root

    # tree now looks like
    #        n3
    #     /      \
    #   n1        n2
    #  /  \      /  \
    # n5   n6  n0    n4

    print(is_complete(n3))  # True
