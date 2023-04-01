from model.calculate import *
import pytest


@pytest.mark.parametrize("text, result",
                         [("45", 1.6197751905438615),
                          ("1", 1.5574077246549023),
                          ("0", 0.0),
                          ("-1.3", -3.6021024479679786)])
def test_math_acos_correct(text, result):
    assert math_tan(text) == result