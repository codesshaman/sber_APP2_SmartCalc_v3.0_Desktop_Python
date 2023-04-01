from model.calculate import *
import pytest


@pytest.mark.parametrize("text, result", [("123.45", 123.45),
                                            ("1", 1),
                                            ("-2", -2),
                                            ("-2.3", -2.3)])
def types_convert_test(text, result):
    assert types_convert(text) == result