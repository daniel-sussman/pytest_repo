import pytest
from lib.present import *

def test_initializes_with_no_contents():
    present = Present()
    assert present.contents == None

def test_can_wrap_a_present():
    present = Present()
    present.wrap('A tricycle')
    assert present.contents == 'A tricycle'

def test_can_unwrap_a_present():
    present = Present()
    present.wrap('A tricycle')
    unwrapped = present.unwrap()
    assert unwrapped == 'A tricycle'

def test_cannot_wrap_a_present_twice():
    present = Present()
    present.wrap('A tricycle')
    with pytest.raises(Exception) as e:
        present.wrap('Some socks')
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_cannot_unwrap_present_with_no_contents():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."