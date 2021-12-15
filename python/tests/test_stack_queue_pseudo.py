from stack_and_queue.stack_and_queue import Node, Stack
from code_challenges.stack_queue_pseudo.stack_queue_pseudo import PseudoQueue
import pytest


node_a = Node('alpha')
node_b = Node('bravo')
node_c = Node('charlie')


# @pytest.mark.skip(reason='not quite time')
def test_all_modules():
    assert Node
    assert Stack
    assert PseudoQueue
    assert PseudoQueue.enqueue
    assert PseudoQueue.dequeue

# @pytest.mark.skip(reason='not quite time')
def test_PsuedoQueue_enqueue_a():
    pseudo_queue = PseudoQueue()
    pseudo_queue.enqueue(node_a)
    assert pseudo_queue.stack_in.top.value == 'alpha'

@pytest.mark.skip(reason='not quite time')
def test_PsuedoQueue_enqueue_b():
    pseudo_queue = PseudoQueue()
    pseudo_queue.enqueue(node_a)
    pseudo_queue.enqueue(node_b)
    assert pseudo_queue.stack_in.top.value == 'bravo'
    assert pseudo_queue.stack_in.top.value.next == 'alpha'


def test_PsuedoQueue_final():
    pass
