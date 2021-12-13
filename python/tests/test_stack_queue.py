from stack_and_queue.stack_and_queue import Node, Stack, Queue
import pytest

node_a = Node('test')
node_b = Node('beta')
node_c = Node('charlie')

# @pytest.mark.skip(reason='not quite time')
def test_stack_and_queue():
    assert Node
    assert Stack.push
    assert Stack.pop
    assert Stack.peek
    assert Stack.is_empty
    assert Queue.enqueue
    assert Queue.dequeue
    assert Queue.peek
    assert Queue.is_empty

def test_stack_top():
    stack = Stack()
    assert stack.top == None

def test_stack_push_a():
    stack = Stack()
    stack.push(node_a)
    actual = stack.top.value
    expected = 'test'
    assert actual == expected

def test_stack_push_b():
    stack = Stack()
    stack.push(node_a)
    stack.push(node_b)
    actual = stack.top.next.value
    expected = 'test'
    assert actual == expected

# @pytest.mark.skip(reason='not quite time')
def test_stack_pop_a():
    stack = Stack()
    stack.push(node_a)
    stack.pop()
    assert stack.top == None

# @pytest.mark.skip(reason='not quite time')
def test_stack_pop_b():
    stack = Stack()
    actual = stack.pop()
    expected = Exception
    assert actual == expected

# @pytest.mark.skip(reason='not quite time')
def test_stack_pop_c():
    stack = Stack()
    stack.push(node_a)
    actual = stack.pop()
    expected = 'test'
    assert actual ==expected

# @pytest.mark.skip(reason='not quite time')
def test_stack_peek_a():
    stack = Stack()
    stack.push(node_a)
    actual = stack.peek()
    expected = 'test'
    assert actual ==expected

# @pytest.mark.skip(reason='not quite time')
def test_stack_peek_b():
    stack = Stack()
    actual = stack.peek()
    expected = Exception
    assert actual ==expected

# @pytest.mark.skip(reason='not quite time')
def test_stack_is_empty_a():
    stack = Stack()
    actual = stack.is_empty()
    expected = True
    assert actual ==expected

# @pytest.mark.skip(reason='not quite time')
def test_stack_is_empty_b():
    stack = Stack()
    stack.push(node_a)
    actual = stack.is_empty()
    expected = False
    assert actual ==expected

# @pytest.mark.skip(reason='not quite time')
def test_complete_final_stack():
    stack = Stack()
    stack.push(node_a)
    stack.pop()
    stack.peek()
    assert stack.peek() == Exception
    assert stack.is_empty() == True

# ---------------- Queue testing -----------------


def test_queue_enqueue_a():
    queue = Queue()
    expected = queue.front
    actual = None
    assert expected == actual

# @pytest.mark.skip(reason='not quite time')
def test_queue_enqueue_b():
    queue = Queue()
    queue.enqueue(node_a)
    actual = queue.front.value
    expected = 'test'
    assert actual == expected

# @pytest.mark.skip(reason='not quite time')
def test_queue_enqueue_c():
    queue = Queue()
    queue.enqueue(node_a)
    queue.enqueue(node_b)
    actual = queue.front.next.value
    expected = 'beta'
    assert actual == expected

@pytest.mark.skip(reason='not quite time')
def test_queue_enqueue_d():
    queue = Queue()
    queue.enqueue(node_a)
    queue.enqueue(node_b)
    queue.enqueue(node_c)
    actual = queue.front.next.next.value
    expected = 'charlie'
    assert actual == expected


@pytest.mark.skip(reason='not quite time')
def test_complete_final_queue():
    queue = Queue()
    queue.enqueue(node_a)
    queue.dequeue()
    queue.peek()
    assert queue.peek() == Exception
    assert queue.is_empty() == True

# @pytest.mark.skip(reason='not quite time')
def test_queue_is_empty_a():
    queue = Queue()
    actual = queue.is_empty()
    expected = True
    assert actual ==expected

# @pytest.mark.skip(reason='not quite time')
def test_queue_is_empty_b():
    queue = Queue()
    queue.enqueue(node_a)
    actual = queue.is_empty()
    expected = False
    assert actual ==expected
