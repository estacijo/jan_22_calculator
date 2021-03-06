"""
Tests the add() function of the calculator
"""

from calculator import add
def test_two_plus_two():
    """
    If given 2 and 2 as parameters, 4 should be returned
    """
    assert add(2, 2) == 4

def test_three_plus_three():
    assert add(3, 3) == 6

def test_no_parameter():
    assert add() == 0

def test_one_two_three():
    """
    Given the values 1, 2, and 3 as parameters
    6 should be returned
    """
    assert add(1, 2, 3) == 6
    
