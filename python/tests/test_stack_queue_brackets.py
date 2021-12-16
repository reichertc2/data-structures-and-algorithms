from code_challenges.stack_queue_brackets.stack_queue_brackets import stack_queue_brackets
import pytest

# Write a function called validate brackets
# Arguments: string
# Return: boolean
# representing whether or not the brackets in the string are balanced



# @pytest.mark.skip(reason='not quite time')
def test_stack_queue_brackets_a():
    value = '()'
    assert stack_queue_brackets(value) == True

# @pytest.mark.skip(reason='not quite time')
def test_stack_queue_brackets_b():
    value = '[]'
    assert stack_queue_brackets(value) == True

# @pytest.mark.skip(reason='not quite time')
def test_stack_queue_brackets_c():
    value = '{}'
    assert stack_queue_brackets(value) == True

# @pytest.mark.skip(reason='not quite time')
def test_stack_queue_brackets_d():
    value = '(test)'
    assert stack_queue_brackets(value) == True

# @pytest.mark.skip(reason='not quite time')
def test_stack_queue_brackets_e():
    value = '[test]'
    assert stack_queue_brackets(value) == True

# @pytest.mark.skip(reason='not quite time')
def test_stack_queue_brackets_f():
    value = '{test}'
    assert stack_queue_brackets(value) == True




# @pytest.mark.skip(reason='not quite time')
def test_stack_queue_brackets_final():
    value_a = '{}'
    value_b = '{}(){}'
    value_c = '()[[Extra Characters]]'
    value_d = '(){}[[]]'
    value_h = '{}{Code}[Fellows](())'
    value_e = '[({}]'
    value_f = '(]('
    value_g = '{(})'
    assert stack_queue_brackets(value_a) == True
    assert stack_queue_brackets(value_b) == True
    assert stack_queue_brackets(value_c) == True
    assert stack_queue_brackets(value_d) == True
    assert stack_queue_brackets(value_h) == True
    assert stack_queue_brackets(value_e) == False
    assert stack_queue_brackets(value_f) == False
    assert stack_queue_brackets(value_g) == False
