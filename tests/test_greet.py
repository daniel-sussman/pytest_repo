from lib.greet import *

def test_greet_greets_me_by_my_name():
    result = greet('Daniel')
    assert result == 'Hello, Daniel!'