from model.calculate import *
import pytest


@pytest.mark.parametrize("result",
                         [(2.718281828459045)])
def test_math_pi_correct(result):
    assert math_e() == result