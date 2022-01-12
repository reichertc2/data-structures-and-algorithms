from hash_table.hash_table import HashTable,HashTableNode
import pytest

# @pytest.mark.skip(reason='not yet')
def test_hash_table_node_a():
    assert HashTableNode

def test_hash_table_node_b():
    node = HashTableNode('test',202)
    actual1 = node.key
    expected1 = 'test'
    actual2 = node.value
    expected2 = 202
    assert actual1 == expected1
    assert actual2 == expected2
    assert node.next == None

# @pytest.mark.skip(reason='not yet')
def test_hash_table_a():
    assert HashTable
    assert HashTable.add
    assert HashTable.get
    assert HashTable.contains
    assert HashTable.hash

# @pytest.mark.skip(reason='not yet')
def test_hash_table_b():
    hash = HashTable(5)
    actual1 = hash.size
    expected1 = 0
    actual2 = hash.capacity
    expected2 = 5
    assert actual1 == expected1
    assert actual2 == expected2
    assert hash.buckets == [None,None,None,None,None]

@pytest.mark.skip(reason='not yet')
def test_hash_table_hash_a():
    hash = HashTable(1024)
    actual = hash.hash()
    expected = TypeError()
    assert actual == expected


# @pytest.mark.skip(reason='not yet')
def test_hash_table_hash_final():
    hash = HashTable(1024)
    actual = hash.hash('test')
    expected = 150
    assert actual == expected
