from model.calculate import *
import pytest


@pytest.mark.parametrize("text, result",
                         [("4", 1.3258176636680326),
                          ("-65", -1.5554129250143014),
                          ("0", 0.0),
                          ("-1.3", -0.9151007005533605)])
def test_math_acos_correct(text, result):
    assert math_atan(text) == result