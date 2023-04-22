import os

import pytest


@pytest.fixture
def twd():
    return os.path.dirname(os.path.realpath(__file__))


@pytest.fixture
def fwd(twd):
    return f'{twd}/fixtures'
