import pytest

from gorgona.stages.base.base_stage import BaseStage
from gorgona.stages.base.replacer import Replacer
from gorgona.stages.base.splitter import Splitter
from gorgona.stages.base.stripper import Stripper


@pytest.fixture()
def setup_replacer():
    r = Replacer(
        '',
        r'a',
        '',
    )

    return r


@pytest.fixture()
def setup_splitter():
    s = Splitter(
        '',
        r' +',
        '@',
    )

    return s


@pytest.fixture()
def setup_stripper():
    s = Stripper('')

    return s


def test_base_stage_instantiation():
    with pytest.raises(TypeError):
        BaseStage('')


def test_replacer_no_matches(setup_replacer):
    assert setup_replacer('bbb') == 'bbb'


def test_replacer_single_match(setup_replacer):
    assert setup_replacer('abb') == 'bb'


def test_replacer_multiple_matches(setup_replacer):
    assert setup_replacer('aba') == 'b'


def test_splitter_no_matches(setup_splitter):
    assert setup_splitter('hello,world') == 'hello,world'


def test_splitter_single_match(setup_splitter):
    assert setup_splitter('hello   world') == 'hello@world'


def test_splitter_multiple_matches(setup_splitter):
    assert setup_splitter('hello  world   again') == 'hello@world@again'


def test_left_strip(setup_stripper):
    assert setup_stripper('  hello') == 'hello'


def test_right_strip(setup_stripper):
    assert setup_stripper('hello  ') == 'hello'


def test__strip(setup_stripper):
    assert setup_stripper('  hello  ') == 'hello'
