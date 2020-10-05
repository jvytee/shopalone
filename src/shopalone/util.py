"""Generally useful helper functions for shopalone"""

from geoalchemy2 import WKBElement
from geoalchemy2.shape import to_shape
from numpy import array


def to_list(element: WKBElement) -> list:
    """Convert a Well-Known-Binary Element to a plain list of points.
    This is useful e.g. if it needs to be serialized as JSON later on.

    :param element: The Well-Known-Binary to convert
    :type element: WKBElement

    :return: A list of coordinates (i.e. list of floats)
    :rtype: list
    """

    return array(to_shape(element)).tolist()
