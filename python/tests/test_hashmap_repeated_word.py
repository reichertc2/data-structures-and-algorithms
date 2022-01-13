from code_challenges.hashmap_repeated_word.hashmap_repeated_word import hashmap_repeated_word
import pytest

# @pytest.mark.skip(reason='not yet')
def test_hashmap_repeated_word_a():
    assert hashmap_repeated_word

# @pytest.mark.skip(reason='not yet')
def test_hashmap_repeated_word_b():
    actual = hashmap_repeated_word('test')
    expected = 'test'
    assert actual == expected

# @pytest.mark.skip(reason='not yet')
def test_hashmap_repeated_word_c():
    actual = hashmap_repeated_word('Test')
    expected = 'test'
    assert actual == expected

# @pytest.mark.skip(reason='not yet')
def test_hashmap_repeated_word_d():
    actual = hashmap_repeated_word('Test,')
    expected = 'test'
    assert actual == expected

# @pytest.mark.skip(reason='not yet')
def test_hashmap_repeated_word_e():
    actual = hashmap_repeated_word('test is a test')
    expected = 'test'
    assert actual == expected


# @pytest.mark.skip(reason='not yet')
def test_hashmap_repeated_word_final_a():
    assert hashmap_repeated_word('Once upon a time, there was a brave princess who...') == 'a'

# @pytest.mark.skip(reason='not yet')
def test_hashmap_repeated_word_final_b():
    assert hashmap_repeated_word('It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...') == 'it'


# @pytest.mark.skip(reason='not yet')
def test_hashmap_repeated_word_final_c():
    assert hashmap_repeated_word('It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...') == 'summer'

