#!/usr/bin/env python3
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a float `multiplier` as an argument and returns a function
    that takes a float as an argument and returns its product with `multiplier`.
    
    Args:
        multiplier (float): The multiplier to be used in the returned function.
    
    Returns:
        Callable[[float], float]: A function that multiplies a float by `multiplier`.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiplies the given `value` by `multiplier`.
        
        Args:
            value (float): The value to be multiplied.
        
        Returns:
            float: The product of `value` and `multiplier`.
        """
        return value * multiplier
    
    return multiplier_function
