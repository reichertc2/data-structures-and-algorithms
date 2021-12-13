from code_challenges.linked_list_zip.linked_list_zip import linked_list_zip
from linked_list.list import LinkedList, Node
import pytest

l_list_a = LinkedList()
l_list_b = LinkedList()
l_list_a.append('A')
l_list_a.append('B')
l_list_a.append('C')
l_list_b.append('1')
l_list_b.append('2')
l_list_b.append('3')

def test_linked_list_zip():
    assert linked_list_zip

# @pytest.mark.skip(reason='not yet')
def test_linked_list_zip_a():
    actual = linked_list_zip(l_list_a, l_list_b)
    expected = l_list_a
    assert actual == expected

@pytest.mark.skip(reason='not yet')
def test_linked_list_zip_a():
    pass
