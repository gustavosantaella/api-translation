# Any ptytest file should start with test_ or end _test
# ptytest methods should start with test_
# Any code should be wrapped in method only
import pytest


@pytest.mark.smoke
def test_firstProgram():
    assert 'hi' == 'hi'

@pytest.mark.skip
def test_firstPrograms():
    assert 'hi' == 'hi'