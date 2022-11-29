import random
from typing import Any, Sequence
from collections.abc import Iterable


class RandomUtils:

    @classmethod
    def get_random_int_value_not_in(cls, max_int: int, not_include: Sequence[int], min_int=0) -> int:
        """
        Generates random integer value that differs from the passed check value
        :args:
         - max_value: max integer value to be generated
         - not_include: sequence of integers that should not be returned
        :optional arg:
         - min_value: int -> min integer value to be generated
        :returns: random integer form the range that is not in not_include sequence
        :raises:
         - ValueError if max_equals min_int
         - ValueError if not_include sequence equals to the range(min_int, max_int)
        """
        not_include = list(not_include) if isinstance(not_include, Iterable) else [not_include]
        available_ints = [num for num in list(range(min_int, max_int)) if num not in not_include]

        if max_int == min_int:
            raise ValueError('max_int cannot be equal min_int')

        return cls.get_random_value_from_sequence_not_in(available_ints, not_include)

    @classmethod
    def get_random_value_from_sequence_not_in(cls, sequence: Sequence[Any], not_include: Sequence) -> Any:
        """
        Returns random value from sequence of values that differs from the passed value
        :args:
         - sequence: sequence with values one of which should be randomly selected
         - not_include: values that should not be returned
        :returns: random element from the sequence not in not_include
        :raises:
         - ValueError if sequence has only one element
         - ValueError if all items from sequence are in not_include
        """
        not_include = list(not_include) if isinstance(not_include, Iterable) else [not_include]
        available_options = [option for option in sequence if option not in not_include]

        if len(sequence) < 2:
            raise ValueError('List of values must contain more than 1 element')
        elif len(available_options) < 1:
            raise ValueError('There is not value to return')

        return random.choice(available_options)
