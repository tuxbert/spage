'''

The 'errors' module handles various cases in which the user of SPAGE
incorrectly uses the library.

'''

def check_mandatory_kwargs(mandatory_arguments, **kwargs):
    """
    Check **kwargs contains all dictionary keys required by the set of
    mandatory arguments.
    """
    keys = set(kwargs.keys())
    
    if not mandatory_arguments.issubset(keys):
        first_missing = next(iter(mandatory_arguments.difference(keys)))
        raise TypeError(f'Missing argument: {first_missing}')
