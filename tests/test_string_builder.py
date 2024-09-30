from lib.string_builder import *

def test_initially_outputs_empty_string():
    builder = StringBuilder()
    assert builder.size() == 0
    assert builder.output() == ""

def test_stringBuilder_is_awesome():
    builder = StringBuilder()
    builder.add("Hello there.")
    result = builder.size()
    assert result == 12
    builder.add(" ")
    builder.add("How we doing?")
    result = builder.size()
    output = builder.output()
    assert result == 26
    assert output == 'Hello there. How we doing?'