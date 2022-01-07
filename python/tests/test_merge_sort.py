from sorts.merge_sort.merge_sort import merge_sort,merge
import pytest


# @pytest.mark.skip(reason='not yet')
def test_merge_sort_a():
    assert merge_sort
    assert merge

@pytest.mark.skip(reason='not yet')
def test_merge_a():
    ls = [10,5]
    actual =  merge(10,5,ls)
    expected = [5,10]
    assert actual == expected
