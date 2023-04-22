from distri import errors, config

import pytest


def test_read_lines_error(twd):
    path = f'{twd}/notfound'

    with pytest.raises(errors.DistriError) as e:
        config.read_lines(path)

    assert str(e.value) == f'[1] path not found: {path}'


def test_read_lines_ok(fwd):
    path = f'{fwd}/config/fedora'

    with open(path, 'r') as f:
        expected =[l.replace('\n', '') for l in f.readlines()]

    current = config.read_lines(path)

    assert current == expected
