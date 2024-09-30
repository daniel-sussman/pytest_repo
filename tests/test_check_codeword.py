from lib.check_codeword import *

def test_check_codeword_accepts_horse():
    result = check_codeword('horse')
    assert result == 'Correct! Come in.'

def test_check_codeword_gently_rejects_house():
    result = check_codeword('house')
    assert result == 'Close, but nope.'

def test_check_codeword_soundly_rejects_gorse():
    result = check_codeword('gorse')
    assert result == 'WRONG!'
