from geoalchemy2 import WKBElement
from geoalchemy2.shape import to_shape
from numpy import array


def to_list(element: WKBElement) -> list:
    return array(to_shape(element)).tolist()
