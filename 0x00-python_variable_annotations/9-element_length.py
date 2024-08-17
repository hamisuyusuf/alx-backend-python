#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple
    contains an element from the iterable
    and the length of that element.

    Parameters:
    lst (Iterable[Sequence]): An iterable of sequences

    Returns A list of tuples, each containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
