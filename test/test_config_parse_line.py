from osri import config


def test_parse_line_error():
    data = 'error?=true'

    assert config.parse_line(data) == ('', '')


def test_parse_line_string_ok():
    data = 'NAME="Fedora Linux"'
    
    assert config.parse_line(data) == ('name', 'Fedora Linux')


def test_parse_line_date_ok():
    data = 'SUPPORT_END=2023-11-14'
    
    assert config.parse_line(data) == ('support_end', '2023-11-14')


def test_parse_line_none_ok():
    data = 'VERSION_CODENAME=""'
    
    assert config.parse_line(data) == ('version_codename', None)

def test_parse_line_quoteless_ok():
    data = 'LOGO=fedora-logo-icon'

    assert config.parse_line(data) == ('logo', 'fedora-logo-icon')
