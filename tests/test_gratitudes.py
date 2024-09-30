from lib.gratitudes import *

def test_initially_returns_empty_string():
    coach = Gratitudes()
    assert coach.format() == "Be grateful for: "

def test_returns_one_thing():
    coach = Gratitudes()
    coach.add('the sun')
    assert coach.format() == "Be grateful for: the sun"

def test_returns_multiple_things():
    coach = Gratitudes()
    coach.add('the sun')
    coach.add('the moon')
    coach.add('the stars')
    assert coach.format() == "Be grateful for: the sun, the moon, the stars"

