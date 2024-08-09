#!/usr/bin/env python3
"""
This module provides an asynchronous list comprehension that
returns a list of floats generated by the async_generator function
from the '0-async_generator' module.
"""
from typing import List
from importlib import import_module as using
async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous list comprehension that returns a list of floats
    generated by the async_generator function.

    Returns:
        List[float]: a list of floats generated by the async_generator.
    """
    return [num async for num in async_generator()]
