import pytest

from gorgona.stages.normalizers import *


@pytest.fixture()
def setup_nfc_unicode_normalizer():
    un = UnicodeNormalizer('', 'NFC')

    return un


@pytest.fixture()
def setup_nfkc_unicode_normalizer():
    un = UnicodeNormalizer('', 'NFKC')

    return un


@pytest.fixture()
def setup_nfd_unicode_normalizer():
    un = UnicodeNormalizer('', 'NFD')

    return un


@pytest.fixture()
def setup_nfkd_unicode_normalizer():
    un = UnicodeNormalizer('', 'NFKD')

    return un


@pytest.fixture()
def setup_whitespace_normalizer():
    ws = WhitespaceNormalizer('')

    return ws


@pytest.fixture()
def setup_lowercaser():
    lc = Lowercaser('')

    return lc


# whitespace
def test_ws_no_whitespaces(setup_whitespace_normalizer):
    assert setup_whitespace_normalizer('abcdef') == 'abcdef'


def test_ws_single_whitespaces(setup_whitespace_normalizer):
    assert setup_whitespace_normalizer('hello world it is me') == 'hello world it is me'


def test_ws_multiple_whitespaces(setup_whitespace_normalizer):
    assert setup_whitespace_normalizer('  hello  world    it      is  me    ') == ' hello world it is me '


# lowercase
def test_lowercaser_all_upper(setup_lowercaser):
    assert setup_lowercaser('ABCDEF') == 'abcdef'


def test_lowercaser_all_lower(setup_lowercaser):
    assert setup_lowercaser('abcdef') == 'abcdef'


def test_lowercaser_mixed(setup_lowercaser):
    assert setup_lowercaser('AbcDEf') == 'abcdef'


def test_unknown_normalization_form():
    with pytest.raises(ValueError):
        UnicodeNormalizer(
            '',
            '',
        )


# nfc
def test_nfc_normal_symbol(setup_nfc_unicode_normalizer):
    assert setup_nfc_unicode_normalizer('a') == 'a'


def test_nfc(setup_nfc_unicode_normalizer):
    assert setup_nfc_unicode_normalizer('C\u0327') == 'Ç'


# nfkc
def test_nfkc_normal_symbol(setup_nfkc_unicode_normalizer):
    assert setup_nfkc_unicode_normalizer('a') == 'a'


def test_nfkc(setup_nfkc_unicode_normalizer):
    assert setup_nfkc_unicode_normalizer('\u2167') == 'VIII'


# nfd
def test_nfd_normal_symbol(setup_nfd_unicode_normalizer):
    assert setup_nfd_unicode_normalizer('a') == 'a'


def test_nfd(setup_nfd_unicode_normalizer):
    assert setup_nfd_unicode_normalizer('\u00C7') == 'Ç'


# nfkd
def test_nfkd_normal_symbol(setup_nfkd_unicode_normalizer):
    assert setup_nfkd_unicode_normalizer('a') == 'a'


def test_nfkd(setup_nfkd_unicode_normalizer):
    assert setup_nfkd_unicode_normalizer('\u2460') == '1'
