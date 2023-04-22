import json

from distri import config, errors

import pytest


def test_load_error(fwd):
    path = f'{fwd}/notfound'

    with pytest.raises(errors.DistriError) as e:
        config.read_lines(path)

    assert str(e.value) == f'[1] path not found: {path}'


def test_load_ok(fwd):
    path = f'{fwd}/config/fedora'

    with open(f'{path}.json', 'r') as f:
        expected = json.load(f)
    current = config.load(path)

    assert current == expected
