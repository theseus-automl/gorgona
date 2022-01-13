from string import punctuation

import pytest

from gorgona.stages.cleaners import SpecialSymbolsCleaner


@pytest.fixture()
def setup_special_symbols_cleaner():
    ssc = SpecialSymbolsCleaner(
        '',
        '',
    )

    return ssc


@pytest.fixture()
def setup_special_symbols_cleaner_with_exceptions():
    ssc = SpecialSymbolsCleaner(
        '',
        '',
        '.,!?'
    )

    return ssc


def test_no_specials_without_exceptions(setup_special_symbols_cleaner):
    assert setup_special_symbols_cleaner('hello world') == 'hello world'


def test_no_specials_with_exceptions(setup_special_symbols_cleaner_with_exceptions):
    assert setup_special_symbols_cleaner_with_exceptions('hello world') == 'hello world'


def test_only_specials_without_exceptions(setup_special_symbols_cleaner):
    assert setup_special_symbols_cleaner(punctuation) == ''


def test_only_specials_with_exceptions(setup_special_symbols_cleaner_with_exceptions):
    assert setup_special_symbols_cleaner_with_exceptions(punctuation) == '!,.?'


def test_mixed_without_exceptions(setup_special_symbols_cleaner):
    assert setup_special_symbols_cleaner('hello, world!?') == 'hello world'


def test_mixed_with_exceptions(setup_special_symbols_cleaner_with_exceptions):
    assert setup_special_symbols_cleaner_with_exceptions('hello, world!?') == 'hello, world!?'
