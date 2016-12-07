
def average(values):
    """computes something
    >>> print (average([20,30,40]))
    30.0
    >>> print (average([20,30,40,40]))
    32.5
    >>> print (average([20,30,40,80]))
    42.5
    """

    return sum(values,0.0)/len(values)

import doctest
doctest.testmod()
