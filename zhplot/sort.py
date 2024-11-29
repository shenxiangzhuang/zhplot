from typing import List, Union

Item = Union[float, int]


def quick_sort(xs: List[Item]) -> List[Item]:
    """
    Quick sort: A very radical implementation

    >>> quick_sort([1, 3, 2, 4, 5])
    [1, 2, 3, 4, 5]
    >>> quick_sort([1.1, 3.3, 2.2, 4.4, 5.5])
    [1.1, 2.2, 3.3, 4.4, 5.5]

    :param xs: comparable list
    :return: sorted list
    """
    return (
        (
            quick_sort([x for x in xs[1:] if x <= xs[0]])
            + [xs[0]]
            + quick_sort([x for x in xs[1:] if x > xs[0]])
        )
        if len(xs) > 1
        else xs
    )
