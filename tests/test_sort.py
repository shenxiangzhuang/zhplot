from typing import List

from hypothesis import Verbosity, given, settings
from hypothesis.strategies import floats, integers, lists, text

from mppt.sort import Item, quick_sort

integer_list = lists(integers(), min_size=0, max_size=50)
float_list = lists(
    floats(allow_nan=False, allow_infinity=False), min_size=0, max_size=50
)
sting_list = lists(text(), min_size=0, max_size=50)


class TestQuickSort:
    @given(items=integer_list)
    @settings(max_examples=100, verbosity=Verbosity.debug)
    def test_integer(self, items: List[Item]):
        assert quick_sort(items) == sorted(items)

    @given(items=float_list)
    @settings(max_examples=300)
    def test_float(self, items: List[Item]):
        assert quick_sort(items) == sorted(items)
