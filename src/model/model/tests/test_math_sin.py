from model.calculate import *
import pytest


@pytest.mark.parametrize("text, result",
                         [("-3", -0.1411200080598672),
                          ("0", 0.0),
                          ("4.3", -0.9161659367494549),
                          ("78", 0.5139784559875352)])
def test_math_sin_correct(text, result):
    assert math_sin(text) == result