import pytest

from distri import errors


def test_simple():
    e = errors.DistriError('myerror')

    assert e.message == 'myerror'
    assert e.code == 1
    assert str(e) == '[1] myerror'


def test_full():
    e = errors.DistriError('myerror', 2)

    assert e.message == 'myerror'
    assert e.code == 2
    assert str(e) == '[2] myerror'


def test_exception():
    with pytest.raises(errors.DistriError):
        raise errors.DistriError('myerror')
