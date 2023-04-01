from model.calculate import *
import pytest


@pytest.mark.parametrize("text, result",
                         [("-3", -0.9899924966004454),
                          ("0", 1.0),
                          ("4.3", -0.40079917207997545),
                          ("7", 0.7539022543433046)])
def test_math_cos_correct(text, result):
    assert math_cos(text) == result