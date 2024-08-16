#!/usr/bin/env python3
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function takes a list of integers and floats `mxd_lst` as an argument 
    and returns their sum as a float.
    """
    return float(sum(mxd_lst))
