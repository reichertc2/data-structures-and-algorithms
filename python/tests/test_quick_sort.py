from sorts.quick_sort import quick_sort
import pytest


# @pytest.mark.skip(reason='not yet')
def test_quick_sort_a():
    assert quick_sort
    # assert partition

def test_quick_sort_final():
    arr = [5,4,3,7,11,12]
    actual = quick_sort(arr,arr[0],12)
    expected = [3,4,5,7,11,12]
    assert actual == expected
