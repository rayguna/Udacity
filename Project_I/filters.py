"""Provide filters for querying close approaches and limit the generated results.

The `create_filters` function produces a collection of objects that is used by
the `query` method to generate a stream of `CloseApproach` objects that match
all of the desired criteria. The arguments to `create_filters` are provided by
the main module and originate from the user's command-line options.

This function can be thought to return a collection of instances of subclasses
of `AttributeFilter` - a 1-argument callable (on a `CloseApproach`) constructed
from a comparator (from the `operator` module), a reference value, and a class
method `get` that subclasses can override to fetch an attribute of interest from
the supplied `CloseApproach`.

The `limit` function simply limits the maximum number of values produced by an
iterator.
"""

import operator
from itertools import islice

#allows to import the datasets to be filtered
from database import NEODatabase
from extract import load_neos, load_approaches

TEST_NEO_FILE = 'test-neos-2020.csv'
TEST_CAD_FILE = 'test-cad-2020.json'


class UnsupportedCriterionError(NotImplementedError):
    """A filter criterion is unsupported."""


def create_filters(
        date=None, start_date=None, end_date=None,
        distance_min=None, distance_max=None,
        velocity_min=None, velocity_max=None,
        diameter_min=None, diameter_max=None,
        hazardous=None
):

    """Create a collection of filters from user-specified criteria.

    Each of these arguments is provided by the main module with a value from the
    user's options at the command line. Each one corresponds to a different type
    of filter. For example, the `--date` option corresponds to the `date`
    argument, and represents a filter that selects close approaches that occurred
    on exactly that given date. Similarly, the `--min-distance` option
    corresponds to the `distance_min` argument, and represents a filter that
    selects close approaches whose nominal approach distance is at least that
    far away from Earth. Each option is `None` if not specified at the command
    line (in particular, this means that the `--not-hazardous` flag results in
    `hazardous=False`, not to be confused with `hazardous=None`).

    The return value must be compatible with the `query` method of `NEODatabase`
    because the main module directly passes this result to that method. For now,
    this can be thought of as a collection of `AttributeFilter`s.

    :param date: A `date` on which a matching `CloseApproach` occurs.
    :param start_date: A `date` on or after which a matching `CloseApproach` occurs.
    :param end_date: A `date` on or before which a matching `CloseApproach` occurs.
    :param distance_min: A minimum nominal approach distance for a matching `CloseApproach`.
    :param distance_max: A maximum nominal approach distance for a matching `CloseApproach`.
    :param velocity_min: A minimum relative approach velocity for a matching `CloseApproach`.
    :param velocity_max: A maximum relative approach velocity for a matching `CloseApproach`.
    :param diameter_min: A minimum diameter of the NEO of a matching `CloseApproach`.
    :param diameter_max: A maximum diameter of the NEO of a matching `CloseApproach`.
    :param hazardous: Whether the NEO of a matching `CloseApproach` is potentially hazardous.
    :return: A collection of filters for use with `query`. Data type is a set. A set of neo or approach list.


    Notes:
        NearEarthObject methods: designation, name, diameter,hazardous; attribute: approaches 
        CloseApproach methods: time, distance, velocity; attributes: _designation, neo

    ref.: python operators - https://docs.python.org/3/library/operator.html
    """
    
    #Need to keep filtering object, depending on the filtering options   
    dictFilters={}
    dictFilters['date']=date
    dictFilters['start_date']=start_date
    dictFilters['end_date']=end_date
    dictFilters['distance_min']=distance_min
    dictFilters['distance_max']=distance_max
    dictFilters['velocity_min']=velocity_min
    dictFilters['velocity_max']=velocity_max
    dictFilters['diameter_min']=diameter_min
    dictFilters['diameter_max']=diameter_max
    dictFilters['hazardous']=hazardous
        
    return dictFilters

def limit(iterator, n=None):
    """Produce a limited stream of values from an iterator.

    If `n` is 0 or None, don't limit the iterator at all.

    :param iterator: An iterator of values.
    :param n: The maximum number of values to produce.
    :yield: The first (at most) `n` values from the iterator.
    """
    
    if n==0 or n==None:
        return iterator
    else:
        #slice the iterator
        return islice(iterator,0,n) 
