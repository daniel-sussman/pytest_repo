import pytest
from lib.password_checker import *

def test_returns_true_when_valid():
    checker = PasswordChecker()
    password = 'I_am_@_t0ta11y_va1id_pa33w0rd'
    assert checker.check(password)

def test_fails_when_password_too_short():
    checker = PasswordChecker()
    password = 'p33w0rd'
    with pytest.raises(Exception) as e:
        checker.check(password)
    error_message = str(e.value)
    assert error_message == 'Invalid password, must be 8+ characters.'

def test_fails_when_password_not_string():
    checker = PasswordChecker()
    password = 3
    with pytest.raises(Exception) as e:
        checker.check(password)
    error_type = str(e.type)
    assert error_type == "<class 'TypeError'>"

def test_fails_when_password_none():
    checker = PasswordChecker()
    password = None
    with pytest.raises(Exception) as e:
        checker.check(password)
    error_type = str(e.type)
    assert error_type == "<class 'TypeError'>"
