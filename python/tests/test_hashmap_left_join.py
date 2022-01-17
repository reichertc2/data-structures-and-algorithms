from code_challenges.hashmap_left_join.hashmap_left_join import hashmap_left_join
import pytest


hashmap_a = {'Dave' : '001' , 'Ava': '002' , 'Joe': '003'}
hashmap_b = {'Dave' : 'Pilot' , 'Ava': 'Nurse' , 'Alex': 'Dog Walker'}
hashmap_c = {'Dave' : '001'}
hashmap_d = {'Dave' : 'Pilot'}
hashmap_e = {'Sally' : 'Doctor'}


# @pytest.mark.skip(reason='not yet')
def test_hashmap_left_join_a():
    assert hashmap_left_join

# @pytest.mark.skip(reason='not yet')
def test_hashmap_left_join_b():
    actual = hashmap_left_join(hashmap_c,hashmap_d)
    expected = [['Dave', '001','Pilot']]
    assert actual == expected

@pytest.mark.skip(reason='not yet')
def test_hashmap_left_join_c():
    actual = hashmap_left_join(hashmap_c,hashmap_e)
    expected = [['Dave', '001',None]]
    assert actual == expected

@pytest.mark.skip(reason='not yet')
def test_hashmap_left_join_final():
    actual = hashmap_left_join(hashmap_a,hashmap_b)
    expected = [['Dave', '001','Pilot'],['Ava','002','Nurse'],['Joe','003',None]]
    assert actual == expected
