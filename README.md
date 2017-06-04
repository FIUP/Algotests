# algotests

*Corpus of `Dati e Algoritmi` Unipd class tests since 2014/15.*

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/licenses/Apache-2.0) [![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)

## Why is it useful?
We tried to write code easy to understand, so even if you don't know how to write code, you can browse the solutions and see how the algorithm works. For example
```shell
def is_max_heap(a):
    """
    :param a: list
        Array organized as max-heap
    :return: bool
        Checks if array a is a max-heap
    """

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
```
is the optimal algorithm to check if the array is a max-heap.



## Questions and issues
The [Github issue tracker](https://github.com/FIUP/algotests/issues) is **only** for bug reports and feature requests. Anything else, such as questions for help, should be posted as `pull request` with detailed motivation.


## Team
[![FIUP](https://avatars2.githubusercontent.com/u/8012686?v=3&s=200)](https://github.com/orgs/FIUP/people)

Wanna join? Why not? Checkout our [github page](https://github.com/FIUP), [drop an email](mailto:fiup.unipd@gmail.com) or follow us [on Facebook](https://www.facebook.com/groups/fiupd/)!


## License
[Apache License](http://www.apache.org/licenses/LICENSE-2.0) Version 2.0, January 2004
