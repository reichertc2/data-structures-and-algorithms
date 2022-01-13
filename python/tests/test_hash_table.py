from hash_table.hash_table import HashTable,Node
import pytest

# @pytest.mark.skip(reason='not yet')
def test_hash_table_node_a():
    assert Node

def test_hash_table_node_b():
    node = Node('test',202)
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

# @pytest.mark.skip(reason='not yet')
def test_hash_table_hash_add_a():
    hash = HashTable(1024)
    hash.add('a',15)
    actual = hash.size
    expected = 1
    assert actual == expected

# @pytest.mark.skip(reason='not yet')
def test_hash_table_hash_add_b():
    hash = HashTable(1024)
    hash.add('a',15)
    hash.add('b',12)
    actual = hash.size
    expected = 2
    assert actual == expected


# @pytest.mark.skip(reason='not yet')
def test_hash_table_hash_add_final():
    hash = HashTable(1024)
    hash.add('a',15)
    actual = hash.buckets[1].value
    expected = 15
    assert actual == expected

def test_hash_table_hash_get_final():
    hash = HashTable(1024)
    hash.add('a',15)
    actual = hash.get('a')
    expected = 15
    assert actual == expected

