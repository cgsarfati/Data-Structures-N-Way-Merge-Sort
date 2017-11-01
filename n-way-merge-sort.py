"""Implementing n-way merge sort where the task is to
sort n already-sorted arrays.

>>> n_way_merge_min_val([[1, 3, 5],[2, 4, 6],[4, 6, 7]])
[1, 2, 4]

>>> n_way_merge_min_val([[1, 3, 5],[2, 4],[4, 6, 7], [2, 3, 4]])
[1, 2, 2, 4]

>>> n_way_merge([[1, 3, 5],[2, 4, 6],[4, 6, 7]])
[1, 2, 3, 4, 4, 5, 6, 6, 7]
"""

from heapq import heappush, heappop
from collections import deque


# Algorithm to Merge K-Sorted List:
#     Take first element of each list and create a min heap.
#     While the min heap has elements. Remove the data from the node and insert to the output list.
#     And get the list index for the Node(index from which list the data came from initially).
#     From the list index, get second element and insert into the min heap.
#     Repeat this process till there are no elements in the heap.


def n_way_merge_min_val(lsts, heap=[]):
    """Using built-in heap for clarity purposes.

    Sort min values for each n already-sorted arrays. """

    # insert 1st elements of each lst to min heap
    cont = True

    while cont:
        for lst in lsts:
            heappush(heap, lst[0])
            cont = False

    # initialize output array
    ordered = []

    # extract min element from heap to output
    while heap:
        ordered.append(heappop(heap))

    return ordered

    # replace extracted element with ned min element from that lst
    # extract min element from heap to output
    # repeat
    # when all but one lst is done, append rest of items to output


def n_way_merge(lsts):
    """ Using priority queue and built-in heap. """

    # initialize priority queue
    pq = []

    # initialize output lst
    result = []

    for lst in lsts:
        lst = deque(lst)
        # take first element of array, and the rest of an array
        heappush(pq, (lst.popleft(), lst))

    while len(pq) > 0:
        key, lst = heappop(pq)
        result.append(key)
        if len(lst) > 0:
            heappush(pq, (lst.popleft(), lst))

    return result


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "All tests passed!"
