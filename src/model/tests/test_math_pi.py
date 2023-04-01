from model.calculate import *
import pytest


@pytest.mark.parametrize("result",
                         [(3.141592653589793)])
def test_math_pi_correct(result):
    assert math_pi() == result