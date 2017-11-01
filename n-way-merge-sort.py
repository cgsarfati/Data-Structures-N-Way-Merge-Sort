"""Implementing n-way merge sort where the task is to
sort n already-sorted arrays.

>>> n_way_merge_builtin([1, 2, 3],
                        [1, 3, 5],
                        [4, 6, 7])
[1, 1, 2, 3, 3, 4, 5, 6, 7]
"""

from heapq import heappush, heappop


def n_way_merge_builtin(lst_of_lsts, heap=[]):
    """Using built-in heap for clarity purposes."""

    # insert 1st elements of each lst to min heap

    # initialize output array

    # extract min element from heap to output
    # replace extracted element with ned min element from that lst
    # extract min element from heap to output
    # repeat
    # when all but one lst is done, append rest of items to output



if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "All tests passed!"
