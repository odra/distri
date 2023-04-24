import pytest

from osri import errors


def test_simple():
    e = errors.OSRIError('myerror')

    assert e.message == 'myerror'
    assert e.code == 1
    assert str(e) == '[1] myerror'


def test_full():
    e = errors.OSRIError('myerror', 2)

    assert e.message == 'myerror'
    assert e.code == 2
    assert str(e) == '[2] myerror'


def test_exception():
    with pytest.raises(errors.OSRIError):
        raise errors.OSRIError('myerror')
