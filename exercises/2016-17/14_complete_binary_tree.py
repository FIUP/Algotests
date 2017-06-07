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
Checks if binary tree is complete.
Solution:
    Assign to each node a int. The root should have 0, the left node of root is 2i + 1, the right node 2i + 2.
    If and only if it's complete then the int assigned to node is <= number of nodes in tree, the tree is complete.
Complexity: O(n)
"""


class BinaryTreeNode(object):
    """ Node of a classic binary tree """

    def __init__(self, key, left=None, right=None):
        """
        :param key: number
            Value of node
        :param left: BinaryTreeNode
            Node at the left of this node
        :param right: BinaryTreeNode
            Node at the right of this node
        """

        object.__init__(self)

        self.key = float(key)
        self.left = left
        self.right = right


def count_nodes(t):
    """
    :param t: BinaryTreeNode
        Node of binary tree
    :return: int
        Number of nodes in tree (including root)
    """

    if t is None:
        return 0

    return count_nodes(t.left) + 1 + count_nodes(t.right)  # left subtree + root + right subtree


def is_binary_tree_complete(t, nodes_count, i=0):
    """
    :param t: BinaryTreeNode
        Node of a binary tree
    :param nodes_count: int
        Nodes in tree
    :param i: int
        Value assigned to node; if i >= nodes_count, then tree's not complete
    :return: bool
        True iff binary tree rooted at given node is complete
        Complexity: O(n), n is the number of nodes in tree.
    """

    if t is None:  # out of bounds (should not happen)
        return True

    if i >= nodes_count:
        return False

    return is_binary_tree_complete(
        t.left,
        nodes_count,
        i=2 * i + 1
    ) and is_binary_tree_complete(
        t.right,
        nodes_count,
        i=2 * i + 2
    )  # check subtrees


if __name__ == '__main__':
    n0 = BinaryTreeNode(6)  # leaf
    n1 = BinaryTreeNode(0)  # first-level left
    n2 = BinaryTreeNode(219, left=n0)  # first-level right
    n3 = BinaryTreeNode(5, left=n1, right=n2)  # root
    # the tree now looks like
    #      n3 (b)
    #     /     \
    #  n1 (r)   n2 (r)
    #          /
    #        n0 (r)
    print(is_binary_tree_complete(n3, count_nodes(n3)))  # false

    n2 = BinaryTreeNode(219, left=None)  # first-level left
    n3 = BinaryTreeNode(5, left=n1, right=n2)  # root
    # the tree now looks like
    #      n3 (r)
    #     /     \
    #  n1 (r)   n2 (b)
    print(is_binary_tree_complete(n3, count_nodes(n3)))  # true
