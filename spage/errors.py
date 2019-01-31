"""

The 'errors' module handles various cases in which the user of SPAGE
incorrectly uses the library.

"""


from typing import Set


def check_extraneous_kwargs(optional_kwargs: Set[str], **kwargs) -> None:
    """
    Check **kwargs contains no more than the possible kwargs.
    """
    keys = set(kwargs.keys())

    if not keys.issubset(optional_kwargs):
        first_extraneous = next(iter(keys.difference(optional_kwargs)))
        raise TypeError(f'Unexpected argument: {first_extraneous}')
