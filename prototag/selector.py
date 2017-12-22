"""selector utilities.
"""


def parse(selector_string=None):
    """Parse the selector from the cli string.

    Paramters
    ---------
    selector_string : string | None
        The input cli string, that specifies the selector.

    Returns
    -------
    array-like, shape(n,)
        Returns an array, where each element corresponds to
        an element in a logical OR clause. Each element is
        itself an array of elements, describing elements in
        a logical AND clause.

    Example
    -------
    The input string 'idea,python:programing' whould result in
    the selector

    .. code-block:: python
        [
            ['idea', 'python'],
            ['programing]
        ]
    """
    if selector_string is None:
        return None

    selector_string = selector_string.strip()
    if selector_string == '':
        return None

    selectors = selector_string.split(':')
    return [f.split(',') for f in selectors]


def validate(result, selectors):
    """Check whether a result does satisfy the selectors

    Parameters
    ----------
    result : (string, dictionary)
        A tuple describing a file with a valid header. The parsed header
        data is saved in the dictionary.

    selectors : array-like, shape (n,)
        The list of selectors.

    Returns
    -------
    bool
        Whether the result does satisfy the selectors.
    """

    for (attribute, selector) in selectors.items():
        data = result[1]

        # Ensure, that the value(s) are extracted as an array.
        if attribute not in data:
            value = []
        else:
            value = result[1][attribute]
            if not hasattr(value, "__len__"):
                value = [value]

        selector_satisfied = False

        for and_condition in selector:
            if all([item in value for item in and_condition]):
                selector_satisfied = True
                break

        if not selector_satisfied:
            return False

    return True


def select_results(results, selector_strings):
    """select the results by the specified selectors.

    Paramters
    ---------
    results : array-like, shape(n,)
        The results after scanning the directory for documents
        with valid headers.

    selector_strings : array-like, shape(m,)
        The list of tuples, that describes the name of the attribute
        and the corresponding selector string.

    Returns
    -------
    array-like, shape(k,)
        The selectored list of results.
    """
    selectors = [(a, parse(s)) for a, s in selector_strings.items()]
    selectors = [(a, s) for a, s in selectors if s is not None]
    selectors = dict(selectors)
    return [r for r in results if validate(r, selectors)]
