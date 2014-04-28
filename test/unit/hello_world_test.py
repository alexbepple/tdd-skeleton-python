from hamcrest import assert_that, is_
import pytest
skip = pytest.mark.skipif


def test_foo():
    assert_that(1+1, is_(2))
    assert 1+1 == 2


@skip
def test_bar():
    assert 1+1 == 3
