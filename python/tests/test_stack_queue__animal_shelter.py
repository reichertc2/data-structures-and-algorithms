
from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter, Dogs, Cats
import pytest
from stack_and_queue.stack_and_queue import Node,Stack

shelter = AnimalShelter()
dog_a = Dogs('spike')
cat_a = Cats('fluffy')
false_cat = 'false'


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
    shelter.enqueue(dog_a)
    actual = shelter.front_dog.value
    expected = True
    assert actual == expected

# @pytest.mark.skip(reason='not quite time')
def test_AnimalShelter_enqueue_c():
    shelter.enqueue(cat_a)
    actual = shelter.front_cat.value
    expected = True
    assert actual == expected

@pytest.mark.skip(reason='not quite time')
def test_AnimalShelter_enqueue_b():
    shelter.enqueue(false_cat)
    actual = shelter.front.value
    expected = Exception
    assert actual == expected







@pytest.mark.skip(reason='not quite time')
def test_stack_queue_animal_shelter_final():
    pass
