from model.calculate import *
import pytest


@pytest.mark.parametrize("text, result", [("2.5*4", 10),
                                          ("-7+3", -4),
                                          ("192/8", 24),
                                          ("7.3-1", 6.3)])
def test_math_eval_correct(text, result):
    assert math_eval(text) == result