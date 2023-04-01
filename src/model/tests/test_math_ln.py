from model.calculate import *
import pytest


@pytest.mark.parametrize("text",
                         [("0"),
                          ("-1"),
                          ("-2.3"),
                          ("-0.3")])
def test_math_ln_errors(text):
    with pytest.raises(ValueError):
        assert math_ln(text)

@pytest.mark.parametrize("text, result",
                         [("1.3", 0.26236426446749106),
                          ("2.1", 0.7419373447293773),
                          ("4.3", 1.4586150226995167),
                          ("7", 1.9459101490553132)])
def test_math_ln_correct(text, result):
    assert math_ln(text) == result