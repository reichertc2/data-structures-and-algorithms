from sorts.insertion_sort import insertion_sort
import pytest

# @pytest.mark.skip(reason='not yet')
def test_insertion_sort_a():
    assert insertion_sort

@pytest.mark.skip(reason='not yet')
def test_insertion_sort_b():
    ls = [5,3,56,44]
    actual = insertion_sort(ls)
    expected = [3,5,44,56]
    assert actual == expected

