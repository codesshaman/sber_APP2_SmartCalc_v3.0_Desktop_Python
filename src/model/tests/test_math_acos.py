from model.calculate import *
import pytest


@pytest.mark.parametrize("text, result",
                         [("-0.33", 1.907099901948877),
                          ("1", 0.0),
                          ("0.36", 1.2025284333582567),
                          ("-1", 3.141592653589793)])
def test_math_acos_correct(text, result):
    assert math_acos(text) == result