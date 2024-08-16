#!/usr/bin/env python3
from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function takes a string `k` and an integer or float `v` as arguments, 
    and returns a tuple where the first element is the string `k`, and the second 
    element is the square of `v`, represented as a float.
    """
    return (k, float(v ** 2))
