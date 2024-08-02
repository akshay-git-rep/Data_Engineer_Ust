import pytest
"""
def capital_case(x):
    if not isinstance(x,str):
        raise TypeError("please provide string arguments")
    return x.capitalize()

def test_capital():
    assert capital_case('Python') == 'Python'

def test_raise_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)
"""
def isEven(num):
    return num % 2

def test_isEven():
    assert isEven(20) == 0
