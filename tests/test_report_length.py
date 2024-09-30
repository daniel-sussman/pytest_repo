from lib.report_length import *
import pytest

def test_reports_five_for_hello():
    result = report_length('hello')
    assert result == "This string was 5 characters long."

def test_reports_zero_for_empty_string():
    result = report_length('')
    assert result == "This string was 0 characters long."

def test_raises_type_error_with_nonstring():
    with pytest.raises(TypeError) as exc_info:
        report_length(5)
        assert exc_info is not None
