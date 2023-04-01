from model.calculate import *
import pytest


@pytest.mark.parametrize("text, result", [(".dot", 0),
                                          ("d.ot", 1),
                                          ("do.t", 2),
                                          ("dot.", 3)])
def test_dot_find_correct(text, result):
    assert dot_find(text) == result


@pytest.mark.parametrize("text, result", [("1dot", -1),
                                          ("d,ot", -1),
                                          ("do:t", -1),
                                          ("!", -1)])
def test_dot_find_without(text, result):
    assert dot_find(text) == result
