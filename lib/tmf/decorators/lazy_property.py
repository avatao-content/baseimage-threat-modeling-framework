# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from functools import update_wrapper


class lazy_property:
    """
    Decorator that replaces a function with the value
    it calculates on the first call.
    """
    def __init__(self, func):
        self.func = func
        update_wrapper(self, func)

    def __get__(self, instance, owner):
        if instance is None:
            return self  # avoids potential __new__ TypeError
        value = self.func(instance)
        setattr(instance, self.func.__name__, value)
        return value
