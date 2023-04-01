from model.calculate import *
import pytest


@pytest.mark.parametrize("text",
                         [("0"),
                          ("-1"),
                          ("-2.3"),
                          ("-0.3")])
def test_math_log_errors(text):
    with pytest.raises(ValueError):
        assert math_log(text)

@pytest.mark.parametrize("text, result",
                         [("1.3", 0.11394335230683678),
                          ("2.1", 0.3222192947339193),
                          ("4.3", 0.6334684555795865),
                          ("7", 0.8450980400142568)])
def test_math_log_correct(text, result):
    assert math_log(text) == result