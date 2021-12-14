from stack_and_queue.stack_and_queue import Node, Stack
from code_challenges.stack_queue_pseudo.stack_queue_pseudo import PseudoQueue
import pytest

# @pytest.mark.skip(reason='not quite time')
def test_all_modules():
    assert Node
    assert Stack
    assert PseudoQueue
    assert PseudoQueue.enqueue
    assert PseudoQueue.dequeue


def test_PsuedoQueue_final():
    pass
