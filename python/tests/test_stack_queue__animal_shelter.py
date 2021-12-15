
from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter, Dogs, Cats
import pytest
from stack_and_queue.stack_and_queue import Node,Stack

shelter = AnimalShelter()
dog_a = Dogs('spike')
dog_b = Dogs('bruno')
cat_a = Cats('fluffy')
false_cat = Node('false')


def test_challenge_initialization():
    assert Node
    assert Stack
    assert AnimalShelter
    assert AnimalShelter.enqueue
    assert AnimalShelter.dequeue
    assert Cats
    assert Dogs

# @pytest.mark.skip(reason='not quite time')
def test_AnimalShelter_enqueue_a():
    shelter.enqueue(dog_a)
    actual = shelter.front_dog.value
    expected = 'spike'
    assert actual == expected

# @pytest.mark.skip(reason='not quite time')
def test_AnimalShelter_enqueue_b():
    actual = shelter.enqueue(dog_a)
    expected = True
    assert actual == expected

# @pytest.mark.skip(reason='not quite time')
def test_AnimalShelter_enqueue_c():
    actual = shelter.enqueue(cat_a)
    expected = True
    assert actual == expected

@pytest.mark.skip(reason='not quite time')
def test_AnimalShelter_enqueue_d():
    actual = shelter.enqueue(false_cat)
    expected = Exception('please add Dog or Cat')
    assert actual == expected

# @pytest.mark.skip(reason='not quite time')
def test_AnimalShelter_enqueue_b():
    shelter.enqueue(dog_a)
    shelter.enqueue(dog_b)
    actual = shelter.front_dog.next.value
    expected = 'bruno'
    assert actual == expected

@pytest.mark.skip(reason='not quite time')
def test_AnimalShelter_dequeue_a():
    actual = shelter.dequeue('cat')
    expected = 'Cat'
    assert actual == expected

@pytest.mark.skip(reason='not quite time')
def test_AnimalShelter_dequeue_b():
    actual = shelter.dequeue('parrot')
    expected = None
    assert actual == expected




@pytest.mark.skip(reason='not quite time')
def test_stack_queue_animal_shelter_final():
    pass
