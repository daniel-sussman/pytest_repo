from lib.counter import *

def test_counter_counts_good():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == 'Counted to 5 so far.'
    counter.add(7)
    result = counter.report()
    assert result == 'Counted to 12 so far.'
    counter.add(-15)
    result = counter.report()
    assert result == 'Counted to -3 so far.'