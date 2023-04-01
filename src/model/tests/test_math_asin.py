from model.calculate import *
import pytest


@pytest.mark.parametrize("text, result",
                         [("-0.3", -0.3046926540153975),
                          ("0", 0.0),
                          ("1", 1.5707963267948966),
                          ("0.3", 0.3046926540153975)])
def test_math_asin_correct(text, result):
    assert math_asin(text) == result

@pytest.mark.parametrize("text",
                         [("-80"),
                          ("-13.1"),
                          ("-2.3"),
                          ("19")])
def test_math_asin_errors(text):
    with pytest.raises(ValueError):
        assert math_asin(text)