'''

The 'errors' module handles various cases in which the user of SPAGE
incorrectly uses the library.

'''

def check_mandatory_kwargs(mandatory_kwargs, **kwargs):
    """
    Check **kwargs contains all dictionary keys required by the set of
    mandatory arguments.
    """
    keys = set(kwargs.keys())
    
    if not mandatory_kwargs.issubset(keys):
        first_missing = next(iter(mandatory_kwargs.difference(keys)))
        raise TypeError(f'Missing argument: {first_missing}')

def check_extraneous_kwargs(mandatory_kwargs, optional_kwargs, **kwargs):
    """
    Check **kwargs contains no more than the possible kwargs.
    """
    possible_kwargs = mandatory_kwargs.union(optional_kwargs)
    keys = set(kwargs.keys())
    
    if not keys.issubset(possible_kwargs):
        first_extraneous = next(iter(keys.difference(possible_kwargs)))
        raise TypeError(f'Unexpected argument: {first_extraneous}')
